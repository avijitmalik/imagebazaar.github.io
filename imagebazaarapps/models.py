from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title 

class Images(models.Model):
    title =  models.CharField(max_length=200)
    description = models.TextField()
    add_date = models.DateField()
    images = models.ImageField(upload_to ="images")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.title


        