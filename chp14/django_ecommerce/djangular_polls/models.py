from django.db import models

# Create your models here.
class Poll(models.Model):
    title=models.CharField(max_length=300)
    publish_date=models.DateTimeField(auto_now=True)

    @property
    def total_votes(self):
        return
        self.poll_items().aggregate(Sum('votes')).get('votes__sum',
        0)

    def poll_items(self):
        return self.items.all()
    # def poll_items(self):
    #     return self.pollitem_set.all()

class PollItem(models.Model):
    poll=models.ForeignKey(Poll, related_name='items')
    name=models.CharField(max_length=40)
    text=models.CharField(max_length=350)
    votes=models.IntegerField(default=0)
    # percentage=models.DecimalField(max_digits=5,
    # decimal_places=2,default=0.0)

    @property
    def percent(self):
        total=self.poll.total_votes
        if total:
            return self.votes/total*100
        return 0

    class Meta:
        ordering=['-text']
