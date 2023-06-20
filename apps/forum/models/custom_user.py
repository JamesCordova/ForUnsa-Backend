from django.db import models
from django.contrib.auth.models import User
from . import Base, Status, School

class CustomUser(User, Base):
    # id, name, last_name, email, nickname, is_admin, is_staff included on User
    current_school = models.ForeignKey(School, on_delete=models.SET_NULL) # School of the user e.g. System Engineering
    biography = models.CharField(max_length=255, blank=True) # description of user
    img = models.ImageField(upload_to='profiles', default='default.jpg')
    is_featured = models.BooleanField(default=False) # user is featured
    semester = models.CharField(max_length=32, default='not defined') # inital semester
    status = models.ForeignKey(Status, on_delete=models.SET_NULL) # Grade status
    slug = models.SlugField(max_length=64, unique=True) # slug for links
    
    class Meta:
        ordering = ['name']
    