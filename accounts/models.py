from django.db import models

# Create your models here.
class Role(models.Model):
    role = models.CharField(
            choices= [
            ('Designer', 'Designer'),
            ('Private user', 'Private user'),
            ],
            max_length=20,
        )
        
    def __str__(self):
        return self.title
        