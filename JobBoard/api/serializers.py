from rest_framework import serializers
from JobBoard.models import JobOffer


class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        exclude = ('id',)
