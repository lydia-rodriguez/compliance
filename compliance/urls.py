from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^ce_list/$', views.ce_list, name='ce_list'),
	url(r'^auth_error/$', views.auth_error, name='auth_error'),
	url(r'^drafts/$', views.ce_draft_list, name='ce_draft_list'),
	url(r'^log/(?P<pk>\d+)/$', views.ce_log_detail, name='ce_log_detail'),
	url(r'^log/new/$', views.ce_log_new, name='ce_log_new'),
	url(r'^log/(?P<pk>\d+)/edit/$', views.ce_log_edit, name='ce_log_edit'),
	url(r'^log/(?P<pk>\d+)/remove/$', views.ce_log_remove, name='ce_log_remove'),
	url(r'^accounts/update/(?P<username>[a-zA-Z0-9]+)/$', views.user_edit, name='user_edit'),
	url(r'^accounts/(?P<username>[a-zA-Z0-9]+)/$', views.get_user_profile, name='user_profile'),
	url(r'^user_list/$', views.user_list, name='user_list'),
]