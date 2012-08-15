#EXPORTAR UM WALL PARA CSV

Pequena App para demonstrar como consumir dados de um mural do redu usando
Python/Django

Foram utilizados:

-Django==1.4.1
-distribute==0.6.27
-dj-database-url==0.2.1
-psycopg2==2.4.5
-rauth==0.4.15
-requests==0.13.8
-simplejson==2.6.1
-wsgiref==0.1.2


#Uso

instale as dependencias

```
$ pip install -r requirements.txt
```

gere o banco de dados

```
$ LOCAL_DEV=True python syncdb
```
rode o servidor

```

