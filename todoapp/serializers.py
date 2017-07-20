from rest_framework import serializers
from todoapp.models import *

from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from django.conf.global_settings import AUTH_USER_MODEL as Account

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoList
        fields = ('id','name','createdDate','user')




class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoItem
        fields = ('id','description', 'status', 'dueByDate', 'todolist')