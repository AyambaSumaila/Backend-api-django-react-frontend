from django.db import models

# Create your models here.
class Todo(models.Model):

    title=models.CharField(max_length=200)
    body=models.TextField(max_length=200)
   # things=models.TextField(max_length=200)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.body
    

    #def __str__(self):
     #   return self.things
