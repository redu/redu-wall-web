from reduRequests import getSpaceData, getTimeline
from HttpClient import HttpClient
import csv

if __name__ == '__main__':
    client = HttpClient("P2AeHTJCV9Wy31Xq8IBIvOpYT1lhbluqvFh8RPdB",
        "SInt2l80rnhz8YkP3zt5ThvKmeb4Srt12EezDIVe")
    client.initClient("keZiAfespsRXlZNS1DKe")
    print ("fetching spaces data...")
    ids = []
    names = []
    spaceData = getSpaceData(client)
    print ("You own the following spaces:")
    for count, space in enumerate(spaceData):
        name = space["name"].encode("UTF-8")
        print ("{0}){1}".format(count, name))
        ids.append(space['id'])
        names.append(name)
    choice = raw_input("Please choose the desired space:")
    timelineData = getTimeline(client, ids[int(choice)])
    f = open("{0}.csv".format(names[int(choice)]), "w")
    writer = csv.writer(f)
    print ("writing file")
    for post in timelineData:
        user = post["user"]
        name = user["first_name"]
        name = name + " " + user["last_name"]
        name = name.encode("UTF-8")
        time = post["created_at"]
        time = time.encode("UTF-8")
        text = post["text"].encode("UTF-8")
        writer.writerow([name, time, text])
    f.close()
    print ("yay! we fineshed exporting your file")
