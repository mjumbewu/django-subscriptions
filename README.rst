====================
Django Subscriptions
====================

**Allow users to subscribe to feeds of information.**

**Author:** Mjumbe Wawatu Ukweli, `Follow me on Twitter`__.

__ twitter_

Overview
========

A reusable app for allowing users to subscribe to feeds of information.

* Let users subscribe to RSS feeds by email
* Send users digests of newly created objects, or of the recent updates to
  existing objects
* Add arbitrary notification channels in addition to email, such as SMS or
  Facebook

Installation
============

Prerequisites:

* Django

If you want to install the latest stable release from PyPi::

    pip install django-subscriptions

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/mjumbewu/django-subscriptions.git#egg=subscriptions

Add ``subscriptons`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'subsctiptions',
    )

Run the South migrations::

    ./manage.py migrate subscriptions


.. _twitter: http://twitter.com/mjumbewu
