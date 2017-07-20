import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")
django.setup()
from todoapp.models import todoList
from todoapp.models import todoItem
from todoapp.models import *
import datetime
from todo.settings import DATABASES
from django.core.management import execute_from_command_line
import MySQLdb

user=DATABASES['default']['USER']
password=DATABASES['default']['PASSWORD']
local='localhost'
db=MySQLdb.connect(local,user,password)
cur=db.cursor()

import click


@click.group()
def start():
    pass

@start.command()
def createdb():
    cur.execute('create database todoDb')
    cur.execute('use todoDb')
    execute_from_command_line(["manage.py","makemigrations"])
    execute_from_command_line(["manage.py", "migrate"])

''''@start.command()
def populatedb():
'''



@start.command()
def dropdb():
    cur.execute('drop database todoDb')


if __name__=='__main__':
    start()