from django.conf.urls import url
from django.contrib.auth import views
from simplemooc.accounts import views as accounts_view

urlpatterns = [
	url(r'^$', accounts_view.dashboard, name='dashboard'),
	url(r'^entrar/$', views.login, {'template_name': 'accounts/login.html'}, name='login'),
	url(r'^registro/$', accounts_view.register, name='register'),
	url(r'^sair/$', views.logout, {'next_page': 'core:home'}, name='logout'),
	url(r'^editar/$', accounts_view.edit, name='edit'),
	url(r'^editar-senha/$', accounts_view.edit_password, name='edit_password'),
]
