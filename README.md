# Django-GameModeShop
Online Shop, create on django. PyCharm. 
If you want start project you need do next steps:

Download file ***Sequrity__.rar*** 

depacking ***my_app копия***

run ***PyCharm***

open Project ***my_app копия***
  
open directory ***my_app копия*** and cut file ***db.sqlite3***

open directory ***~../my_app копия/mainapp/migrations/*** and delete all, pust file ***__ іnit__.py*** 

now open terminal in PyCharm and write next commands:

```pip install -r requirements.txt```

Now write next commands in **directory ~../my_app копия>

```python manage.py makemigrations``` - its make db.sqlite3 and some migrations

```python manage.py migrate``` - its create table in you db.sqlite3

**Now we need to replace the db.sqlite3 with the one we cut earlier**
~~_______________________________________________________________________________________________________~~

**Now we can start our site:

```python manage.py runserver```

*open link and our site working*

` #TELEGRAMM @Shakal11052002 `
