from enroll.models import User
from enroll.api.serializer import UserSerialzer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerialzer
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

