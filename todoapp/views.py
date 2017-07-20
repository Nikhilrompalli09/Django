# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from django.contrib.auth import
from todoapp.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import *
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

# Create your views here.
from django.http import HttpResponse,Http404



'''rest api'''

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from todoapp.serializers import *
from rest_framework import authentication, permissions


def get_object(self):
    obj = get_object_or_404(self.get_queryset())
    self.check_object_permissions(self.request, obj)
    return obj



class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(request, *args, **kwargs)


def home(request):
    return render(request,'todoapp/list_template.html')




class UserTodoLists(CSRFExemptMixin,APIView):
     """
        List all snippets, or create a new snippet.
    """

     authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication,BasicAuthentication]
     permission_classes =  (permissions.IsAuthenticated,)

     def get(self, request, format=None):                   #retrive all lists of a user using user id
        id=request.user.id
        print id
        list = todoList.objects.all().filter(user_id=id)
        serializer = ListSerializer(list, many=True)
        # request.method='GET'
        return Response(serializer.data)


     def post(self, request, format=None):                  #create a new list
        item=request.data
        print item
        print request.user.id
        # item["user"]=request.user.id
        # print item
        list={}
        list["name"]=request.data["name"]
        list["createdDate"]=request.data["createdDate"]
        list["user"]=request.user.id
        # print list
        serializer = ListSerializer(data=list)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class TodoList(CSRFExemptMixin,APIView):
    """
        List all snippets, or create a new snippet.
        """

    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes =  (permissions.IsAuthenticated,)

    def get(self, request,pk, format=None):                     #accessing the items in perticular list based on list id
        # id=request.user.id
        # print id
        list = todoItem.objects.all().filter(todolist__id=pk)
        serializer = ItemSerializer(list, many=True)
        # request.method='GET'
        return Response(serializer.data)

    def post(self, request, pk,format=None):                    #adding new item to list
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):                #updating list by list id
        listItems = todoList.objects.get(pk=pk)
        # print "list"
        # print listItems
        # data = JSONParser().parse(request)
        data = request.data
        newData={}
        newData['name']=data['name']
        newData['user'] = request.user.id
        print(newData)
        serializer = ListSerializer(listItems, data=newData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):         #deleting list by list id
        newList = todoList.objects.get(pk=pk)
        newList.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)



class TodoListItem(CSRFExemptMixin,APIView):
    """
            List all snippets, or create a new snippet.
            """

    # authentication_classes = []
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication]
    # permission_classes = []
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request,pk, format=None):             #retrive item details using item id
        # id = request.user.id
        list = todoItem.objects.all().filter(pk=pk)
        serializer = ItemSerializer(list, many=True)
        # request.method='GET'
        return Response(serializer.data)

    def put(self, request,pk, format=None):             #update item details using item id

        listItems=todoItem.objects.get(pk= pk)
        # print "list"
        # print listItems
        data = JSONParser().parse(request)
        # print(listItems)
        serializer = ItemSerializer(listItems,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # deleting item using item id
        newList = todoItem.objects.get(pk= pk)
        newList.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
























# @csrf_exempt
# def allTodoList(request):
#     list = todoList.objects.all()
#     if request.method == 'GET':
#         serializer = ListSerializer(list, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ListSerializer(list,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


'''2nd views'''
# class allListView(ListView):
#     model=todoList
#     template_name = "todoapp/allLists.html"
#     context_object_name = 'lists'
#
#
# class UserListView(DetailView):
#     model=todoList
#     template_name = "todoapp/allLists.html"
#     context_object_name = 'lists'
#
#     def get_context_data(self, **kwargs):
#         context = super(UserListView, self).get_context_data(**kwargs)
#         context['lists'] = todoList.objects.all().filter(user__id=self.object.id)
#         return context
#
# class listAndItemsView(ListView):
#     model=todoList
#     template_name = "todoapp/listAndItems.html"
#     context_object_name = 'lists'
#
#     def get_context_data(self, **kwargs):
#         context = super(listAndItemsView, self).get_context_data(**kwargs)
#         context['data'] = todoItem.objects.all().values('description','status','dueByDate','todolist__name','todolist__createdDate')
#         return context
#
#
# class ItemsView(DetailView):
#     # slug_field = 'userName'
#     model=todoList
#     #model=User
#     template_name = "todoapp/itemsById.html"
#     context_object_name = 'item'
#     def get_context_data(self, **kwargs):
#         context = super(ItemsView, self).get_context_data(**kwargs)
#         #self.object
#         context['data'] = todoItem.objects.values('description', 'status', 'dueByDate').filter(todolist__id=self.object.id)
#         return context
#
#
# class CreateListItem(LoginRequiredMixin,CreateView):
#     model =todoItem
#     fields = ('description','status','dueByDate','todolist')
#     success_url = reverse_lazy('allLists')
#
# class CreateList(LoginRequiredMixin,CreateView):
#     model =todoList
#     fields = ('name','createdDate','user')
#     success_url = reverse_lazy('allLists')
#
# class updateListItem(UpdateView):
#     model =todoItem
#     fields = ('description','status','dueByDate','todolist')
#     success_url = reverse_lazy('allLists')
#
#
# class DeleteList(DeleteView):
#     model = todoList
#     context_object_name = 'list'
#     success_url = reverse_lazy('allLists')
#







'''def allLists(request):
    lists=todoList.objects.all()
    context={'lists':lists}
    return render(request, 'todoapp/allLists.html', context)

def items(request,id):
    item=todoItem.objects.all().values('description','status','dueByDate').filter(todolist_id__id=id)
    itemName = todoList.objects.get(id=id)
    context = {'item': item, 'itemame': itemName}
    return render(request, 'todoapp/itemsById.html', context)'''
