from django.conf.urls.defaults import patterns, include, url
from subscriptions.api.views import SubscriptionIndex, ContentFeedRecordIndex

urlpatterns = patterns('',
    url('^subscriptions/$', SubscriptionIndex.as_view()),
    url('^feed_records/$', ContentFeedRecordIndex.as_view()),
)
