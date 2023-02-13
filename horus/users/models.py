from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username, name, email, password=None):
        if not username:
            raise TypeError("user manager should has username.")
        if not email:
            raise TypeError("user manager should has email.")
        if not name:
            raise TypeError("user manager should has name.")
        if not password:
            raise TypeError("you should add password.")

        user = self.model(
            email=self.normalize_email(email), name=name, username=username
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, name, email, password=None):
        if not username:
            raise TypeError("you should add username.")
        if not email:
            raise TypeError("you should add email.")
        if not name:
            raise TypeError("you should add name.")
        if not password:
            raise TypeError("you should add password.")

        user = self.model(
            email=self.normalize_email(email), name=name, username=username
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("Username"), max_length=100, unique=True)
    name = models.CharField(_("Full Name"), max_length=255, db_index=True)
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    is_verified = models.BooleanField(_("Is user verified by email"), default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name"]

    objects = UserManager()

    def __str__(self):
        return self.username





class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return str(self.image)
    
    @classmethod
    def get_default(cls):
        return cls.objects.first()



class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile_name', on_delete=models.CASCADE)
    picture = models.ForeignKey(ImageUpload, related_name='profile_picture', on_delete=models.SET_NULL, null=True, blank=True, db_constraint=False)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    bio = models.TextField(default='I am a user')
    code_country = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @property
    def email(self):
        return self.user.email

    @property
    def username(self):
        return self.user.username
    
    @property
    def full_name(self):
        return self.user.name

    def __str__(self) -> str:
        return self.user.email
    