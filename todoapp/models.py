# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

#user = foreginkey(user)

# Create your models here.
class todoList(models.Model):
    name = models.CharField(max_length=128)
    createdDate=models.DateField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.name

class todoItem(models.Model):
    # itemName=models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    status=models.BooleanField(default=False)
    dueByDate=models.DateField(null=True, blank=True)
    todolist=models.ForeignKey(todoList,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.description