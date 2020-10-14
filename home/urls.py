from django.urls import path
from . import views
from home.dash_apps.finished_apps import simpleexample


urlpatterns = [
    # path('', views.home, name='home'),
    path("checkout", views.checkout, name="checkout"),
	path("logout", views.logout_request, name= "logout_request"),
	path("login", views.login_request, name= "logout_request"),
	path("register", views.register, name="register"),
	path("create-sub", views.create_sub, name="create sub"), #add
	path("complete", views.complete, name="complete"), #add
]