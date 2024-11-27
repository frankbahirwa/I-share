from django.contrib.auth.models import AbstractUser, Group, Permission, UserManager
from django.db import models


class CustomUserManager(UserManager):
    """Custom manager to handle the creation of users and superusers."""

    def create_user(self, username, password=None, **extra_fields):
        """Create and return a regular user with a username and password."""
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """Create and return a superuser with a username and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom user model extending AbstractUser."""
    # Additional fields
    email = models.EmailField(unique=True, blank=False, max_length=255)
    profile = models.ImageField(upload_to="images/profiles/", blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Override related_name for groups and user_permissions to avoid conflict
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Custom related_name
        blank=True
    )

    objects = CustomUserManager()

    # Use username as the primary authentication field
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
