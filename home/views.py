from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import (
    HeroSection,
    Route,
    HeroSlider,
    ContactSettings,
    Booking,
)

from .forms import BookingForm


# ==========================
# HOME PAGE
# ==========================

def home(request):

    hero = HeroSection.objects.first()

    routes = Route.objects.filter(
        is_active=True
    )

    sliders = HeroSlider.objects.filter(
        is_active=True
    )

    # ==========================
    # BOOKING
    # ==========================

    if request.method == "POST":

        if not request.user.is_authenticated:

            return redirect(
                "/login/?next=/#booking"
            )

        form = BookingForm(
            request.POST
        )

        if form.is_valid():

            booking = form.save()

            return redirect(
                "booking_contact",
                booking_id=booking.id
            )

    else:

        form = BookingForm()

    return render(
        request,
        "home.html",
        {
            "hero": hero,
            "routes": routes,
            "sliders": sliders,
            "form": form,
        },
    )


# ==========================
# REGISTER
# ==========================

def register_view(request):

    # Already logged in
    if request.user.is_authenticated:

        return redirect("home")

    if request.method == "POST":

        email = request.POST.get(
            "email",
            ""
        ).strip().lower()

        password = request.POST.get(
            "password",
            ""
        )

        confirm_password = request.POST.get(
            "confirm_password",
            ""
        )

        # EMAIL
        if not email:

            return render(
                request,
                "register.html",
                {
                    "error":
                        "Please enter your email."
                }
            )

        # PASSWORD
        if not password:

            return render(
                request,
                "register.html",
                {
                    "error":
                        "Please enter your password."
                }
            )

        # PASSWORD MATCH
        if password != confirm_password:

            return render(
                request,
                "register.html",
                {
                    "error":
                        "Passwords do not match."
                }
            )

        # PASSWORD LENGTH
        if len(password) < 6:

            return render(
                request,
                "register.html",
                {
                    "error":
                        "Password must be at least 6 characters."
                }
            )

        # CHECK USER
        if User.objects.filter(
            username=email
        ).exists():

            return render(
                request,
                "register.html",
                {
                    "error":
                        "This email is already registered."
                }
            )

        # CREATE USER
        User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # IMPORTANT:
        # Automatic login nahi hoga

        return redirect("login")

    return render(
        request,
        "register.html"
    )


# ==========================
# LOGIN
# ==========================

def login_view(request):

    # Already logged in
    if request.user.is_authenticated:

        return redirect("home")

    next_url = request.GET.get(
        "next",
        ""
    )

    if request.method == "POST":

        email = request.POST.get(
            "email",
            ""
        ).strip().lower()

        password = request.POST.get(
            "password",
            ""
        )

        # EMPTY EMAIL
        if not email:

            return render(
                request,
                "login.html",
                {
                    "error":
                        "Please enter your email.",
                    "next":
                        next_url,
                }
            )

        # EMPTY PASSWORD
        if not password:

            return render(
                request,
                "login.html",
                {
                    "error":
                        "Please enter your password.",
                    "next":
                        next_url,
                }
            )

        # AUTHENTICATE
        user = authenticate(
            request,
            username=email,
            password=password
        )

        # SUCCESS
        if user is not None:

            login(
                request,
                user
            )

            if next_url:

                return redirect(
                    next_url
                )

            return redirect(
                "home"
            )

        # FAILED
        return render(
            request,
            "login.html",
            {
                "error":
                    "Invalid email or password.",
                "next":
                    next_url,
            }
        )

    return render(
        request,
        "login.html",
        {
            "next":
                next_url
        }
    )


# ==========================
# LOGOUT
# ==========================

def logout_view(request):

    logout(request)

    # Logout ke baad Login page
    return redirect("login")


# ==========================
# SERVICES
# ==========================

def services(request):

    return render(
        request,
        "services.html"
    )


# ==========================
# BOOKING CONTACT
# ==========================

def booking_contact(
    request,
    booking_id
):

    if not request.user.is_authenticated:

        return redirect(
            f"/login/?next=/booking-contact/{booking_id}/"
        )

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    contact = ContactSettings.objects.first()

    if request.method == "POST":

        return redirect(
            "booking_success"
        )

    return render(
        request,
        "booking_contact.html",
        {
            "booking":
                booking,
            "contact":
                contact,
        },
    )


# ==========================
# BOOKING SUCCESS
# ==========================

def booking_success(request):

    if not request.user.is_authenticated:

        return redirect(
            "login"
        )

    return render(
        request,
        "booking_success.html"
    )