from django.urls import path
from django.contrib.auth import views as auth_views
from .views import display_co2_data, render_json_response


urlpatterns = [
    path("", display_co2_data, name="display_co2_data"),
    path("fetch-json/", render_json_response, name="render_json_response"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
]
