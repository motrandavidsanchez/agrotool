from django.contrib import admin
from django.urls import path, include

from agrotool.router import router

urlpatterns = [
    path('admin/', admin.site.urls),

    # Urls Apis
    path('api/v1/', include(router.urls)),
]
