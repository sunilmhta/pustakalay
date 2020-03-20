from django.conf.urls import url
from .import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout

urlpatterns=[
	url(r'^$',views.home),
	url(r'^login/$', LoginView.as_view(template_name='blog/login.html'), name='login'),
	url(r'^logout/$', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
	url(r'^register/$',views.register,name='register'),
	url(r'^profile/$',views.profile,name='profile'),

]