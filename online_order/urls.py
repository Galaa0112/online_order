
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('signup/',RegisterView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('about/',AboutUsView.as_view(),name='about'),
    path('terms/',TermsView.as_view(),name='terms'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('password/',ChangePasswordView.as_view(),name='password'),
    path('order/',OrderView.as_view(), name='order'),
    path('list/',OrderListView.as_view(), name='list'),
    path('<str:id>/update/',OrderUpdateView.as_view(), name='update'),
    path('<str:id>/order_cancel/',OrderCancelView.as_view(), name='order_cancel'),
    path('msg/',MessageRequestView.as_view(),name='msg'),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    
]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)