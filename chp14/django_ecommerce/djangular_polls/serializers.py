from rest_framework import serializers
from djangular_polls.models import *

class PollItemSerializer(serializers.ModelSerializer):
    percentage=serializers.IntegerField(source='percent')
    class Meta:
        model=PollItem
        fields=('id','poll','name','text','votes','percentage')

class PollSerializer(serializers.ModelSerializer):
    items=PollItemSerializer(many=True, required=False)
    total_vote=serializers.IntegerField(source='total_votes')

    class Meta:
        model=Poll
        fields=('title','publish_date','items','total_vote')
