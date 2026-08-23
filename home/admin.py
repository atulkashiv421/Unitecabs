from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

from .models import (
    HeroSection,
    Route,
    HeroSlider,
    ContactSettings,
    Booking,
    LoginUser,
)


# =====================================================
# HERO SECTION
# =====================================================

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):

    list_display = (
        "heading",
        "from_city",
        "to_city",
    )


# =====================================================
# ROUTES
# =====================================================

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):

    list_display = (
        "from_city",
        "to_city",
        "price",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "from_city",
        "to_city",
    )


# =====================================================
# HERO SLIDER
# =====================================================

@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "is_active",
    )

    list_filter = (
        "is_active",
    )


# =====================================================
# CONTACT SETTINGS
# =====================================================

@admin.register(ContactSettings)
class ContactSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "whatsapp_number",
        "email",
    )


# =====================================================
# BOOKINGS
# =====================================================

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "trip_type",
        "pickup",
        "drop",
        "phone",
        "pickup_date",
        "status",
    )

    list_filter = (
        "status",
        "trip_type",
    )

    search_fields = (
        "pickup",
        "drop",
        "phone",
    )


# =====================================================
# CHECK CURRENTLY LOGGED-IN USERS
# =====================================================

def get_logged_in_users():

    logged_in_users = set()

    sessions = Session.objects.filter(
        expire_date__gte=timezone.now()
    )

    for session in sessions:

        session_data = session.get_decoded()

        user_id = session_data.get(
            "_auth_user_id"
        )

        if user_id:

            logged_in_users.add(
                str(user_id)
            )

    return logged_in_users


# =====================================================
# LOGIN USERS
# =====================================================

@admin.register(LoginUser)
class LoginUserAdmin(admin.ModelAdmin):

    list_display = (
        "email",
        "login_status",
        "last_login",
        "created_at",
        "is_logged_in",
    )

    search_fields = (
        "email",
    )

    list_filter = (
        "is_logged_in",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "email",
        "created_at",
        "last_login",
        "login_status",
    )


    # =================================================
    # LOGIN STATUS
    # =================================================

    @admin.display(
        description="Login Status"
    )
    def login_status(self, obj):

        logged_in_users = get_logged_in_users()

        try:

            user = User.objects.get(
                email=obj.email
            )

            if str(user.id) in logged_in_users:

                return "🟢 Currently Logged In"

            return "⚪ Logged Out"

        except User.DoesNotExist:

            return "⚪ Logged Out"


# =====================================================
# REMOVE DEFAULT DJANGO USERS
# =====================================================

try:

    admin.site.unregister(User)

except admin.sites.NotRegistered:

    pass