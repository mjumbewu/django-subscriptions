from django.forms import Textarea
from jsonfield.fields import JSONFormField
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from subscriptions.models import Subscription, ContentFeedRecord

class ContentFeedRecordSerializer (ModelSerializer):
    class Meta (object):
        model = ContentFeedRecord


class ContentFeedRecordField (PrimaryKeyRelatedField):
    pass


class SubscriptionSerializer (ModelSerializer):
    feed_record = ContentFeedRecordSerializer()
#    feed_record = ModelField(model_field=Subscription.feed_record, widget=Textarea())

    class Meta (object):
        model = Subscription
        fields = ('id', 'subscriber', 'feed_record',)
