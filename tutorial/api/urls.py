from django.urls import path, include

from . views import ListUsers, once,  UserList

urlpatterns = [
    path('', ListUsers.as_view()),
    path('once/', once),
    path('gen/', UserList.as_view()),
    path('products/', include('products.urls'))
]