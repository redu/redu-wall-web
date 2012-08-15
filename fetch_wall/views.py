# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import slugify
from reduApi.HttpClient import HttpClient
from reduApi.reduRequests import getTimeline, getSpaceData
from reduApi.writer import exportTimeline
from datetime import datetime

globalClient = HttpClient('P2AeHTJCV9Wy31Xq8IBIvOpYT1lhbluqvFh8RPdB',
            'SInt2l80rnhz8YkP3zt5ThvKmeb4Srt12EezDIVe')


def redu_csv(request):
    if request.session.get('requestClient'):
        spaces = []
        requestClient = request.session["requestClient"]
        if request.session.get('spaces'):
            spaces = request.session['spaces']
        else:
            spaces = getSpaceData(requestClient)
            request.session['spaces'] = spaces
            request.session.save()
        return render_to_response('redu_csv.html', {'spaces': spaces,
         "refresh_url": reverse("fetch_wall.views.refresh_spaces")},
            context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('fetch_wall.views.get_pin'))


def get_pin(request):
    if request.POST:
        code = request.POST['code']
        requestClient = HttpClient('P2AeHTJCV9Wy31Xq8IBIvOpYT1lhbluqvFh8RPdB',
         'SInt2l80rnhz8YkP3zt5ThvKmeb4Srt12EezDIVe')
        requestClient.initClient(code)
        request.session['requestClient'] = requestClient
        request.session.save()
        return HttpResponseRedirect(reverse('fetch_wall.views.redu_csv'))
    else:
        return render_to_response('get_pin.html',
            {'url': globalClient.getAuthorizeUrl()},
            context_instance=RequestContext(request))


def clear_cookies(request):
    request.session.clear()
    return HttpResponse("Cookies limpos")


def show_space(request):
    space = request.session['spaces'][int(request.POST['choice']) - 1]
    space_id = space['id']
    space_name = space['name']
    filename = space_name + str(datetime.now())
    filename = slugify(filename)
    requestClient = request.session['requestClient']
    posts = getTimeline(requestClient, space_id)
    response = HttpResponse(mimetype='text/csv')

    response['Content-Disposition'] =  \
    'attachment; filename={0}.csv'.format(filename)
    exportTimeline(response, posts)
    return response


def refresh_spaces(request):
    if request.session.get("spaces"):
        del request.session['spaces']
        request.session.save()
    return HttpResponseRedirect(reverse("fetch_wall.views.redu_csv"))
