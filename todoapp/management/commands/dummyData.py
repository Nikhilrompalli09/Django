from django.core.management.base import BaseCommand, CommandError
from todoapp.models import *
import datetime
class Command(BaseCommand):

    def handle(self,*args,**options):
        lists=[]

        lists.append(todoList(name="office work"))
        lists.append(todoList(name="learning work"))
        lists.append(todoList(name="application"))
        lists.append(todoList(name="missionrnd"))
        lists.append(todoList(name="hostelwork"))
        for i in lists:
            i.save()
            for j in range(5):
                todoItem(description=i.name+str(j),dueByDate='2017-06-23',todolist=i).save()