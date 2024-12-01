from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import routers, permissions

from tracker import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Tracker API",
        default_version="v1",
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r"boards", views.BoardViewSet)
router.register(r"employees", views.EmployeeViewSet)
router.register(r"tasks", views.TaskViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
