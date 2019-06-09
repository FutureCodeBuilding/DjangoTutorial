from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
	re_path(r'products/(?P<productId>\d+)', views.products, name='product'),
	re_path(r'products/$', views.products, name='product'),

	re_path(r'users/(?P<id>\d+)/(?P<name>\D+)', views.users, name='user'),
	re_path(r'users/$', views.users, name='user'),

	# re_path(r'^about', views.about, name='about'),
    path("about/", TemplateView.as_view(template_name="Polls/about.html",extra_context={"text" : "About me and my beatyfull site"})),
	re_path(r'^contact', views.contact, name='contact'),

	re_path(r'^details', views.details, name='details'),
	path('', views.index, name='home'),
	path('create/', views.create),
]

# urlpatterns = [
#     path('products/<int:productid>/', views.products),
#     path('users/<int:id>/<name>/', views.users),
# ]
