from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # ==========================
    # ADMIN
    # ==========================

    path(
        "admin/",
        admin.site.urls
    ),

    # ==========================
    # HOME APP
    # ==========================

    path(
        "",
        include("home.urls")
    ),

]


# =========================================================
# STATIC FILES
# =========================================================

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)


# =========================================================
# MEDIA FILES
# =========================================================

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)