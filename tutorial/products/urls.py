from django.urls import path

from . views import ListProduct

urlpatterns = [
    path('', ListProduct.as_view())
]