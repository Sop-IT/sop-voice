from django.urls import reverse

from utilities.testing import TestCase
from circuits.models import Provider
from dcim.models import Site

from sop_phone.models import *


class SopPhoneViewTestCaseMixin:

    user_permissions = ()
    tab = False
    tab_param = None
    model = None
    VIEW_PERM = None
    ADD_PERM = None
    EDIT_PERM = None


    def get_action_url(self, action, instance=None):
        """reverse sop phone plugin url with action"""
        url = f'plugins:{self.model._meta.app_label}:{self.model._meta.model_name}_{action}'

        if instance is None:
            return reverse(url)

        return reverse(url, kwargs={'pk': instance.pk})


    def test_list_no_perm(self):
        """test list view no perm"""
        url = self.get_action_url('list')

        response = self.client.get(url)
        self.assertHttpStatus(response, 403)


    def test_list_perm(self):
        """test list view perm"""
        url = self.get_action_url('list')

        self.add_permissions(self.VIEW_PERM)
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)


    def test_add_no_perm(self):
        """test add view no perm"""
        url = self.get_action_url('add')

        response = self.client.get(url)
        self.assertHttpStatus(response, 403)


    def test_add_perm(self):
        """test add view perm"""
        url = self.get_action_url('add')

        self.add_permissions(self.ADD_PERM)
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)


    def test_detail_no_perm(self):
        """test detail no perm"""
        instance = self.model.objects.first()
        url = self.get_action_url('detail', instance)

        response = self.client.get(url)
        self.assertHttpStatus(response, 403)


    def test_detail_perm(self):
        """test detail perm"""
        instance = self.model.objects.first()
        url = self.get_action_url('detail', instance)

        self.add_permissions(self.VIEW_PERM)
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)


    def test_edit_no_perm(self):
        """test edit no perm"""
        instance = self.model.objects.first()
        url = self.get_action_url('edit', instance)

        response = self.client.get(url)
        self.assertHttpStatus(response, 403)


    def test_edit_perm(self):
        """test detail perm"""
        instance = self.model.objects.first()
        url = self.get_action_url('edit', instance)

        self.add_permissions(self.EDIT_PERM)
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)


    def test_tab_view_no_perm(self):
        """test tab no perm"""
        if self.tab is False:
            return

        instance = Site.objects.first()
        url = f'/dcim/sites/{instance.pk}/{self.tab_param}/'

        self.add_permissions('dcim.view_site')
        response = self.client.get(url)
        self.assertHttpStatus(response, 403)


    def test_tab_view_perm(self):
        """test tab perm"""
        if self.tab is False:
            return

        instance = Site.objects.first()
        url = f'/dcim/sites/{instance.pk}/{self.tab_param}/'

        self.add_permissions('dcim.view_site')
        self.add_permissions(self.VIEW_PERM)
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)



class PhoneMaintainerViewTestCase(TestCase, SopPhoneViewTestCaseMixin):

    model = PhoneMaintainer
    VIEW_PERM = 'sop_phone.view_phonemaintainer'
    ADD_PERM = 'sop_phone.add_phonemaintainer'
    EDIT_PERM = 'sop_phone.change_phonemaintainer'

    @classmethod
    def setUpTestData(cls):

        maintainer = PhoneMaintainer(name='SALUT', slug='salut', status='active')
        maintainer.full_clean()
        maintainer.save()



class PhoneDeliveryViewTestCase(TestCase, SopPhoneViewTestCaseMixin):

    model = PhoneDelivery
    VIEW_PERM = 'sop_phone.view_phonedelivery'
    ADD_PERM = 'sop_phone.add_phonedelivery'
    EDIT_PERM = 'sop_phone.change_phonedelivery'

    @classmethod
    def setUpTestData(cls):

        site = Site.objects.create(name="salut", slug="salut")
        site.full_clean()
        site.save()

        provider = Provider.objects.create(name="salut", slug="salut")
        provider.full_clean()
        provider.save()

        delivery = PhoneDelivery(
            delivery="TEST_METHOD",
            provider=provider,
            site=site,
            status="active",
            ndi=33123456789
        )
        delivery.full_clean()
        delivery.save()


class PhoneDIDViewTestCase(TestCase, SopPhoneViewTestCaseMixin):

    model = PhoneDID
    VIEW_PERM = 'sop_phone.view_phonedid'
    ADD_PERM = 'sop_phone.add_phonedid'
    EDIT_PERM = 'sop_phone.change_phonedid'

    @classmethod
    def setUpTestData(cls):

        site = Site.objects.create(name="salut", slug="salut")
        site.full_clean()
        site.save()

        provider = Provider.objects.create(name="salut", slug="salut")
        provider.full_clean()
        provider.save()

        delivery = PhoneDelivery(
            delivery="TEST_METHOD",
            provider=provider,
            site=site,
            status="active",
            ndi=33123456789
        )
        delivery.full_clean()
        delivery.save()

        did = PhoneDID(
            start=33123456780,
            end=33123456788,
            site=site,
            delivery=delivery
        )
        did.full_clean()
        did.save()

