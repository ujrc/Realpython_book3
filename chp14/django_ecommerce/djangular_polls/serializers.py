from rest_framework import serializers
from djangular_polls.models import Poll, PollItem


class PollItemSerializer(serializers.ModelSerializer):
    percentage = serializers.Field(source='percent')

    class Meta:
        model = PollItem
        fields = ('id', 'poll', 'name', 'text', 'votes', 'percentage')


class PollSerializer(serializers.ModelSerializer):
    items = PollItemSerializer(many=True, required=False)
    total_vote = serializers.Field(source='total_votes')

    class Meta:
        model = Poll
        fields = ('id', 'title', 'publish_date', 'items', 'total_vote')