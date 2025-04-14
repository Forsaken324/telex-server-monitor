from rest_framework.views import APIView
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from . serializers import UserSerialiser

from . throttles import OncePerDayUserThrottle

# class based views

class ListUsers(APIView):
    """
        View to list all users in the system.
    """

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
    

# function based views

@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def once(request):
    return Response({"message" : "Hello for today! see you tomorror!"})


# generic based views

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = [permissions.IsAdminUser]

    