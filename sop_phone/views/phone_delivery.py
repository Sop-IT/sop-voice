from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404

from utilities.permissions import get_permission_for_model
from utilities.views import GetRelatedModelsMixin

from netbox.views import generic
from dcim.models import Site

from sop_phone.forms.phone_delivery import PhoneDeliveryForm, PhoneDeliveryFilterForm, PhoneDeliveryBulkEditForm
from sop_phone.tables.phone_delivery import PhoneDeliveryTable
from sop_phone.filtersets import PhoneDeliveryFilterSet
from sop_phone.models import PhoneDelivery, PhoneDID, PhoneInfo
from sop_phone.utils import format_number_flag


__all__ =  (
    'PhoneDeliveryEditView',
    'PhoneDeliveryDetailView',
    'PhoneDeliveryDeleteView',
    'PhoneDeliveryBulkEditView',
    'PhoneDeliveryDeleteView',
    'PhoneDeliveryListView',
    'PhoneDeliverySiteView'
)


class PhoneDeliveryListView(generic.ObjectListView):
    queryset = PhoneDelivery.objects.all()
    table = PhoneDeliveryTable
    filterset = PhoneDeliveryFilterSet
    filterset_form = PhoneDeliveryFilterForm


class PhoneDeliveryBulkEditView(generic.BulkEditView):
    queryset = PhoneDelivery.objects.all()
    table = PhoneDeliveryTable
    form = PhoneDeliveryBulkEditForm
    filterset = PhoneDeliveryFilterSet


class PhoneDeliveryBulkDeleteView(generic.BulkDeleteView):
    queryset = PhoneDelivery.objects.all()
    table = PhoneDeliveryTable
    filterset = PhoneDeliveryFilterSet


class PhoneDeliveryDetailView(GetRelatedModelsMixin, PermissionRequiredMixin, generic.ObjectView):
    '''
    returns the Phone Delivery detail page with context
    '''
    queryset = PhoneDelivery.objects.all()
    permission_required=get_permission_for_model(PhoneDelivery, "view")

    def get_extra_context(self, request, instance) -> dict:
        context: dict = {}

        dids = PhoneDID.objects.filter(delivery=instance)

        try:
            site_info = PhoneInfo.objects.filter(site=instance.site.id)
            context['maintainer'] = site_info.first().maintainer
        except:pass
        if instance.ndi:
            context['ndi'] = format_number_flag(instance.ndi)
        if instance.dto:
            context['dto'] = format_number_flag(instance.dto)
        context['did_range'] = PhoneDID
        context['num_range'] = dids.count()
        context['num_did'] = PhoneDelivery.count_dids(dids)
        context['related_models'] = self.get_related_models(
            request, instance,
        )
        return context


class PhoneDeliveryEditView(generic.ObjectEditView):
    '''
    creates anew Phone Delivery instance
    '''
    queryset = PhoneDelivery.objects.all()
    form = PhoneDeliveryForm


class PhoneDeliveryDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView ):
    '''
    deletes a Phone Delivery object
    '''
    queryset = PhoneDelivery.objects.all()
    permission_required=get_permission_for_model(PhoneDelivery, "delete")


class PhoneDeliverySiteView(generic.ObjectEditView):
    '''
    adds a site automatically to the Phone Delivery
    '''
    queryset = PhoneDelivery.objects.all()
    form = PhoneDeliveryForm

    def get_object(self, **kwargs):
        return self.queryset.model(site=get_object_or_404(Site, pk=kwargs['pk']))

    def alter_object(self, obj, request, args, kwargs):
        pk = kwargs.get('pk')
        site = get_object_or_404(Site, pk=pk)
        obj = self.queryset.model
        return obj(site=site)

    def get(self, request, *args, **kwargs): 
        '''
        get request handler
        '''
        response = super().get(request, *args, **kwargs)
        return response
