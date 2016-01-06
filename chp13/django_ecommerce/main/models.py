from django.db import models
from django.utils import timezone

# Create your models here.
class MarketingItem(models.Model):
    img_name=models.CharField(max_length=250)
    heading=models.CharField(max_length=320)
    caption=models.TextField()
    button_title=models.CharField(max_length=25, default=" View details")
    button_link=models.URLField(null=True, default='register')

class StatusReport(models.Model):
    user=models.ForeignKey('payments.User')# used to avoid circular reference payments.models import User
    when=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=200)


class Announcement(models.Model):
    title=models.CharField(max_length=50)
    publication_date=models.DateTimeField(timezone.now())
    image=models.CharField(max_length=300, null=True)
    vid=models.URLField(null=True)
    content=models.TextField()

class Badge(models.Model):
    name=models.CharField(max_length=80)
    image=models.CharField(max_length=300)
    description=models.TextField()

    class Meta:
        ordering=('name',)
