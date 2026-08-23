from django.urls import path
from . import views


urlpatterns = [

    # ==========================
    # HOME PAGE
    # ==========================

    path(
        "",
        views.home,
        name="home"
    ),


    # ==========================
    # LOGIN
    # ==========================

    path(
        "login/",
        views.login_view,
        name="login"
    ),


    # ==========================
    # REGISTER
    # ==========================

    path(
        "register/",
        views.register_view,
        name="register"
    ),


    # ==========================
    # LOGOUT
    # ==========================

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),


    # ==========================
    # SERVICES
    # ==========================

    path(
        "services/",
        views.services,
        name="services"
    ),


    # ==========================
    # BOOKING CONTACT
    # ==========================

    path(
        "booking-contact/<int:booking_id>/",
        views.booking_contact,
        name="booking_contact"
    ),


    # ==========================
    # BOOKING SUCCESS
    # ==========================

    path(
        "booking-success/",
        views.booking_success,
        name="booking_success"
    ),

]