from django.db import models
import datetime

# Create your models here.

class Requestmodel(models.Model):
    # buyer = models.ForeignKey('Profile', on_delete=models.CASCADE)
    request = models.TextField()
    graphic_type = models.CharField(
        choices= [
        ('Poster', 'poster'),
        ('Icon', 'icon'),
        ('Logo', 'logo'),
        ('Different', 'different'),
        ],
        default='Logo',
        max_length=9,
    )
    deadline = models.DateTimeField()
    date_requested = models.DateTimeField(auto_now_add=True)
    wireframe = models.ImageField(default='default.png', blank=True)
    
    
    def __str__(self):
        return self.title
        
    def snippet(self):
        return self.request[:50] + '...'
        
        
    class Quotes(models.Model):
        # order = models.OneToOneField('Requestmodel', on_delete=models.CASCADE)
        price= models.DecimalField(max_digits=10, decimal_places=2)
        status = models.CharField(
            choices= [
            ('Pending', 'Pending'),
            ('Accepted', 'Accepted'),
            ('Rejected', 'Rejected'),
            ],
            default='Pending',
            max_length=8,
        )
        # designer = models.ForeignKey('Profile', on_delete=models.CASCADE)
        delivered = models.BooleanField()