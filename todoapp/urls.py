from django.conf.urls import url
from todoapp import views

urlpatterns=[
    #url(r'$',views.welcome),
    #url(r'^todoLists/',views.allLists,name='allLists'),


    url(r'^todoLists/$',views.UserTodoLists.as_view(),name='UserLists'),
    url(r'^todoList/(?P<pk>[0-9]+)/$',views.TodoList.as_view(),name='List'),
    url(r'^todoListItem/(?P<pk>[0-9]+)/$',views.TodoListItem.as_view(),name='ListItem'),
    url(r'^Home/$',views.home,name='home'),


    # '''class based views'''


    # url(r'^todoLists/$',views.allListView.as_view(),name='allLists'),
    #  url(r'^todoList/(?P<pk>[0-9]+)/$',views.ItemsView.as_view(),name='itemsDetails'),
    #  url(r'^todoList/user/(?P<pk>[0-9]+)/$',views.UserListView.as_view(),name='userDetails'),
    #  url(r'^todoListItems/$',views.listAndItemsView.as_view(),name='listAndItems'),
    #  url(r'^todoList/createItem/$',views.CreateListItem.as_view(),name='createItems'),
    #  url(r'^todoList/createList/$',views.CreateList.as_view(),name='createList'),
    #

    # url(r'^todoList/update/(?P<pk>[0-9]+)/$',views.updateListItem.as_view(),name='updateItems'),
    # url(r'^todoList/delete/(?P<pk>[0-9]+)/$',views.DeleteList.as_view(),name='deleteList'),
    #



    #url(r'^todoList/(?P<id>[0-9]+)/$', views.items,name='items'),
    #url(r'^todoList/(?P<id>[0-9]+)/$', views.items,name='items'),
]


