from rest_framework import viewsets

from gwaithdemo.models import Rate
from gwaithdemo.serializers import RateSerializer


class RateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rates to be viewed or edited.
    """
    queryset = Rate.objects.all().order_by('currency', '-date')
    serializer_class = RateSerializer
