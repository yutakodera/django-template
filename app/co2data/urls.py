from django.urls import path
from django.contrib.auth import views as auth_views
from .views import co2_data_table, Co2DataListCreateView


urlpatterns = [
    # APIエンドポイント
    path("api/", Co2DataListCreateView.as_view(), name="co2data-api"),
    # WebアプリのURL
    path("table/", co2_data_table, name="co2data-table"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="co2data/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
]
