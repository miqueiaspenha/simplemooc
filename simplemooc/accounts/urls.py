from django.conf.urls import url
from django.contrib.auth import views
from simplemooc.accounts import views as accounts_view

urlpatterns = [
	url(r'^entrar/$', views.login, {'template_name': 'accounts/login.html'}, name='login'),
	url(r'^registro/$', accounts_view.register, name='register'),
]
