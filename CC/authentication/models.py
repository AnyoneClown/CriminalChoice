from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
import datetime

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'mafia'),
    (2, 'gang'),
    (3, 'admin'),
)

GANG_RANK_CHOICES = (
    (1, 'Youngsta'),
    (2, 'Beginner'),
    (3, 'Checked Up'),
    (4, 'Hustler'),
    (5, 'Hoodlum'),
    (6, 'Black Flawless'),
    (7, 'Outlaw'),
    (8, 'Authority'),
    (9, 'Deputy Pac'),
    (10, 'Strawberry Pac'),
)

MAFIA_RANK_CHOICES = (
    (1, 'Novizio'),
    (2, 'Associato'),
    (3, 'Controllato'),
    (4, 'Razionale'),
    (5, 'Testato'),
    (6, 'Soldato'),
    (7, 'Capo'),
    (8, 'Sotoo Capo'),
    (9, 'Destra Boss'),
    (10, 'Consigliere'),
    (11, 'Don'),
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        role = extra_fields.get('role', 0)
        if role == 1:
            user.rank = MAFIA_RANK_CHOICES[0][0]
        elif role ==2:
            user.rank = GANG_RANK_CHOICES[0][0]

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 3)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default = 0)
    rank = models.IntegerField(default=0)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.role == 1:
            self.rank = MAFIA_RANK_CHOICES[0][0]
        elif self.role ==2:
            self.rank = GANG_RANK_CHOICES[0][0]

        super().save(*args, **kwargs)