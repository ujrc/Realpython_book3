from rest_framework import serializers
from djangular_polls.models import *

class PollItemSerializer(serializers.ModelSerializer):
    percentage=serializers.Field(source='percent')
    class Meta:
        model=PollItem
        fields=('id','poll','name','text','votes','percentage')

class PollSerializer(serializers.ModelSerializer):
    items=PollItemSerializer(many=True, required=False)
    total_vote=serializers.Field(source='total_votes')

    class Meta:
        model=Poll
        fields=('title','publish_date','items','total_vote')
