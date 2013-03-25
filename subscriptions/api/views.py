from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from subscriptions.api.serializers import SubscriptionSerializer, ContentFeedRecordSerializer
from subscriptions.models import Subscription, ContentFeedRecord


class SubscriptionIndex (ListCreateAPIView):
    model = Subscription
    serializer_class = SubscriptionSerializer


class ContentFeedRecordIndex (ListCreateAPIView):
    model = ContentFeedRecord
    serializer_class = ContentFeedRecordSerializer
