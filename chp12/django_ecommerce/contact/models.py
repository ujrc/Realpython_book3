from django.db import models
from django.utils import timezone
#import datetime
# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    topic = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField( default=timezone.now#auto_now_add=True#, default=datetime.datetime.now
    #The options auto_now, auto_now_add, and default are mutually exclusive. Only one of these options may be present.
    )

    def __str__(self):
        #    def __unicode__(self): py2x
        return self.email

    class Meta:
        ordering = ['-timestamp']
