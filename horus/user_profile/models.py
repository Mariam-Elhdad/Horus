from django.db import models

from horus.users.models import User

# Create your models here.
# dummy change


class ImageUpload(models.Model):
    image = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return str(self.image)

    @classmethod
    def get_default(cls):
        return cls.objects.first()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name="profile_name", on_delete=models.CASCADE
    )
    picture = models.OneToOneField(
        ImageUpload,
        related_name="profile_picture",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_constraint=False,
    )
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    bio = models.TextField(default="I am a user")
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
