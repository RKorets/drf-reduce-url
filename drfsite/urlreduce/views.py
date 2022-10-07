from django.contrib.auth.models import User
from django.db.models import F
from django.http import HttpResponseRedirect
from rest_framework import generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Url
from .permissions import IsOwnerOrReadOnly
from .serializers import UrlSerializer, RegisterUserSerializer


# Custom pagination class
class UrlPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ShortViewSet(APIView):
    """
    short/<str:short>
    """
    def get(self, request, short):
        short = self.kwargs.get('short')
        get_original = Url.objects.filter(short__icontains=short).first()
        if get_original is None:
            return HttpResponseRedirect(redirect_to='https://google.com')
        get_original.views = F('views') + 1
        get_original.save()
        return HttpResponseRedirect(redirect_to=f'{get_original}')


class UrlApiRUD(generics.RetrieveUpdateDestroyAPIView):
    """
    api/v1/r/<int:pk>
    """
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


class UrlAPIList(generics.ListCreateAPIView, mixins.UpdateModelMixin):
    """
    api/v1/urllist/
    """
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = UrlPagination

    def get_queryset(self):
        if self.request.user.is_staff:
            return Url.objects.all()
        user = self.request.user
        return Url.objects.filter(user=user)


class UrlAPIUpdate(generics.RetrieveUpdateAPIView):
    """
    api/v1/u/<int:pk>
    """
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = (IsAdminUser, IsOwnerOrReadOnly)


class RegistrationAPIView(generics.CreateAPIView):
    """
    api/v1/registrations/
    """
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterUserSerializer


class CreateUrlAPIView(generics.CreateAPIView):
    """
    api/v1/create/
    """
    queryset = Url.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UrlSerializer
