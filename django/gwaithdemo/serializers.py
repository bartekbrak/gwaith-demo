from rest_framework import serializers

from gwaithdemo.models import Rate


class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rate
        fields = ('date', 'rate', 'currency')
