from django.db import models

# Create your models here.
class UserPddrodddddfile(models.Model):
    role = models.CharField(
                choices= [
                ('Designer', 'I want to design'),
                ('User', 'I want to buy designs'),
                ],
                max_length=20,
            )
        
    def __str__(self):
        return self.user.username
