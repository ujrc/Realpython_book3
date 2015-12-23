from django.db import models

# Create your models here.
class MarketingItem(models.Model):
    img_name=models.CharField(max_length=250)
    heading=models.CharField(max_length=320)
    caption=models.TextField()
    button_title=models.CharField(max_length=25, default=" View details")
    button_link=models.URLField(null=True, default='register')
