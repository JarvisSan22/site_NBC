
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your views here.

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin



"""
class UserManager(BaseUserManager):
    
    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)        
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # Add other fields here

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
"""

class Tag(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self) -> str:
        return super().__str__()

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #Photos
    #ToDo
    prediction_data = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  


class Image(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.SET_NULL,null=True)
    #user = models.ForeignKey(User, default=None, on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    #LatLong 
    lat = models.DecimalField('lat',max_digits=8, decimal_places=6,null=True)
    lng = models.DecimalField('lng',max_digits=9, decimal_places=6,null=True)