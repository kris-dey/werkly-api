from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.core.exceptions import PermissionDenied

# Create your views here.

class UserListView(generics.ListAPIView):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer

class UserProfile(generics.RetrieveUpdateDestroyAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication,)
	permission_classes = (IsAuthenticated,)
	serializer_class = serializers.UserProfileSerializer

	def get_queryset(self):
		users = models.User.objects.get(id=self.kwargs['pk'])
		if self.request.user == users:
			queryset = models.User.objects.all()
			return queryset
		else:
			PermissionDenied

	def perform_update(self,serializer_class):
		users = models.User.objects.get(id=self.kwargs['pk'])
		if self.request.user == users:
			serializer_class.save()
		else:
			PermissionDenied

def perform_delete(self,serializer_class):
    users = models.User.objects.get(id=self.kwargs['pk'])
    if self.request.user == users:
        instance.delete
        update_index.Command().handle(using=['default'],remove=True)
    else:
        PermissionDenied
