from django.db import models

# Create your models here.
class Post(models.Model):
    author=models.CharField( max_length=50)
    title=models.CharField( max_length=50)
    description=models.TextField()
    created_on=models.DateTimeField( auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title+"/n"+self.description
    