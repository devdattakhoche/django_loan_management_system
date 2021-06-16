from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UploadFile(models.Model):
    file = models.FileField(upload_to="pdf/files")


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email,
            is_staff=True,
            is_superuser=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            **kwargs,
        )
        user.set_password(password)
        user.save()
        return user


# Create your models here.
class User(AbstractUser):

    roles = [("Admin", "Admin"), ("Agent", "Agent"), ("Customer", "Customer")]
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
    email = models.EmailField(_("email"), unique=True)
    user_id = models.BigAutoField(primary_key=True, unique=True, null=False)
    username = models.CharField(default=None, null=True, max_length=10)
    role = models.CharField(choices=roles, default="Customer", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    # @classmethod
    def save_customer(self, *args, **kwargs):
        if not self.pk:
            self.role = "Customer"
        self.save(*args, **kwargs)

    def save_agent(self, *args, **kwargs):
        if not self.pk:
            self.role = "Agent"
        self.save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super(User, self).save(*args, **kwargs)

    def save_admin(self, *args, **kwargs):
        if not self.pk:
            self.role = "Admin"
        self.save(*args, **kwargs)

    def __str__(self):
        return "{self.name}_{self.role}".format(self=self)
