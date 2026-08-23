
from django.db import models


class HeroSection(models.Model):

    heading = models.CharField(
        max_length=200
    )

    subheading = models.CharField(
        max_length=300
    )

    from_city = models.CharField(
        max_length=100,
        default="Chandigarh"
    )

    to_city = models.CharField(
        max_length=100,
        default="Anywhere"
    )

    hero_image = models.ImageField(
        upload_to="hero/"
    )

    def __str__(self):
        return self.heading


class Route(models.Model):

    from_city = models.CharField(
        max_length=100
    )

    to_city = models.CharField(
        max_length=100
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to="routes/"
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.from_city} → {self.to_city}"


class HeroSlider(models.Model):

    title = models.CharField(
        max_length=100,
        blank=True
    )

    image = models.ImageField(
        upload_to="hero_slider/"
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):

        if self.title:
            return self.title

        return f"Slider {self.id}"


class ContactSettings(models.Model):

    whatsapp_number = models.CharField(
        max_length=20
    )

    email = models.EmailField()

    message = models.TextField(
        default=(
            "Once your booking request is received, "
            "our team will contact you within 1–2 hours "
            "to confirm your booking."
        )
    )

    def __str__(self):
        return "Contact Settings"


class Booking(models.Model):

    # =========================================
    # TRIP TYPE
    # =========================================

    TRIP_TYPES = (
        ("One Way", "One Way"),
        ("Round Trip", "Round Trip"),
    )

    trip_type = models.CharField(
        max_length=20,
        choices=TRIP_TYPES
    )

    # =========================================
    # LOCATIONS
    # =========================================

    pickup = models.CharField(
        max_length=200
    )

    drop = models.CharField(
        max_length=200
    )

    # =========================================
    # PICKUP DATE & TIME
    # =========================================

    pickup_date = models.DateField()

    pickup_time = models.TimeField()

    pickup_ampm = models.CharField(
        max_length=2,
        choices=(
            ("AM", "AM"),
            ("PM", "PM"),
        ),
        default="AM"
    )

    # =========================================
    # RETURN DATE & TIME
    # =========================================

    return_date = models.DateField(
        null=True,
        blank=True
    )

    return_time = models.TimeField(
        null=True,
        blank=True
    )

    return_ampm = models.CharField(
        max_length=2,
        choices=(
            ("AM", "AM"),
            ("PM", "PM"),
        ),
        null=True,
        blank=True
    )

    # =========================================
    # CONTACT
    # =========================================

    phone = models.CharField(
        max_length=15
    )

    # =========================================
    # BOOKING INFORMATION
    # =========================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    # =========================================
    # DISPLAY
    # =========================================

    def __str__(self):
        return f"{self.pickup} → {self.drop}"


# =====================================================
# LOGIN USERS
# =====================================================

class LoginUser(models.Model):

    email = models.EmailField(
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    last_login = models.DateTimeField(
        null=True,
        blank=True
    )

    is_logged_in = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.email