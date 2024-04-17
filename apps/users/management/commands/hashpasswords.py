from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    help = "Hashes user passwords"  # python manage.py hashpasswords

    def handle(self, *args, **kwargs):
        for user in User.objects.filter(type="Requester"):
            user.password = make_password(user.password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f"Password for {user.email} was hashed successfully!")
            )
