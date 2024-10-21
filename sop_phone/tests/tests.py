from django.test import TestCase

from dcim.models import Site

from .models import *


class PhoneDIDTests(TestCase):

    def add_right_data(self):
        obj = PhoneDID.objects.create(site=)
