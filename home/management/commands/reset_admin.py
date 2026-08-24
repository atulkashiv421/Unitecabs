from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Reset admin password"

    def handle(self, *args, **options):
        User = get_user_model()

        username = "nikhil"
        new_password = "atul123q1"

        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Password updated for {username}"
            )
        )