from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save

class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    # Define unique related_names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='app_users',  # Change this to a unique related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='app_users',  # Change this to a unique related_name
        blank=True,
    )

    objects = AppUserManager()

    def __str__(self):
        return self.username

class UserPayment(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	payment_bool = models.BooleanField(default=False)
	stripe_checkout_id = models.CharField(max_length=500)


@receiver(post_save, sender=AppUser)
def create_user_payment(sender, instance, created, **kwargs):
	if created:
		UserPayment.objects.create(app_user=instance)