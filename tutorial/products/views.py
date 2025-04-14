from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from . models import Product
from . serializers import ProductSerializer

class ListProduct(APIView):

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request, format=None):
        # products = [
        #     {
        #         "title": product.title,
        #         "content": product.content,
        #         "price": product.price
        #     }
        #     for product in Product.objects.all()
        # ]  # hard coded way of doing it
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
