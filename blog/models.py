from django.db import models
from django.utils import timezone
#user -> post is 1:n relationship, 1 user can have many posts
from django.contrib.auth.models import User 
#database is modelled as a class with the data members being attributes

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.title
