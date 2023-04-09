from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path('signup/', views.signup_view, name='signup'),
    path("personality/", views.personality_view, name="personality"),
    path("internship/", views.internship_view, name="internship"),
    path("selector/", views.selector_view, name="selector"),
]