from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # Custom user manager implementation
    def create_user(request):
        username = models.CharField(max_length=50)
        role = models.CharField(default="user", max_length=50)
        password = models.CharField(max_length=50)
        created_date = models.DateTimeField(auto_created=True)
        updated_date = models.DateTimeField(auto_now_add=True)

        # USERNAME_FILED = 'username'
        # REQUIRED_FIELDS = ['username']

class CustomUser(AbstractBaseUser):
    USERNAME_FIELD = 'username'  # Replace 'username' with your desired field
    # Rest of the custom user model implementation
    user_manager = UserManager()
    user = user_manager.create_user()
# Create your models here.
    
    
