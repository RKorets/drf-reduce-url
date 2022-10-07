from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

urlpatterns = [
    # edit - only author or administrator [post, put, delete, get], any only read [get]
    path('api/v1/r/<int:pk>', views.UrlApiRUD.as_view(), name='rud'),
    # only authorizations user, only [post] method
    path('api/v1/create/', views.CreateUrlAPIView.as_view(), name='create'),

    # only administrator permission. only [post] method
    path('api/v1/registrations/', views.RegistrationAPIView.as_view(), name='registrations'),

    #  short url -> redirect original url, [get] method
    path('short/<str:short>', views.ShortViewSet.as_view(), name='short_redirect'),

    # only admin permission [get] method
    path('api/v1/urllist/', views.UrlAPIList.as_view(), name='admin_all_list'),

    # only admin permission or obj own
    path('api/v1/u/<int:pk>', views.UrlAPIUpdate.as_view(), name='admin_or_author_update'),


    # [post] method - create token/ access and refresh
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
