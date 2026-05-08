from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404

from utilities.permissions import get_permission_for_model

from netbox.views import generic
from dcim.models import Site

from sop_phone.forms.phone_did import PhoneDIDForm, PhoneDIDFilterForm, PhoneDIDBulkEditForm, PhoneDIDBulkImportForm
from sop_phone.tables.phone_did import PhoneDIDTable
from sop_phone.filtersets import PhoneDIDFilterSet
from sop_phone.models import PhoneDID, PhoneInfo
from sop_phone.utils import format_number_flag


__all__ = (
    'PhoneDIDEditView',
    'PhoneDIDDeleteView',
    'PhoneDIDDetailView',
    'PhoneDIDBulkEditView',
    'PhoneDIDBulkDeleteView',
    'PhoneDIDListView',
    'PhoneDIDBulkImportView',
    'PhoneDIDAddSiteView'
)


class PhoneDIDListView(generic.ObjectListView):
    '''
    all DIDs list
    '''
    queryset = PhoneDID.objects.all()
    table = PhoneDIDTable
    filterset_form = PhoneDIDFilterForm
    filterset = PhoneDIDFilterSet


class PhoneDIDBulkEditView(generic.BulkEditView):
    '''
    for the "edit selected" view
    '''
    queryset = PhoneDID.objects.all()
    table = PhoneDIDTable
    form = PhoneDIDBulkEditForm
    filterset = PhoneDIDFilterSet


class PhoneDIDBulkDeleteView(generic.BulkDeleteView):
    '''
    for the "delete selected" view
    '''
    queryset = PhoneDID.objects.all()
    table = PhoneDIDTable
    filterset = PhoneDIDFilterSet


class PhoneDIDEditView(generic.ObjectEditView):
    '''
    edits a DID instance
    '''
    queryset = PhoneDID.objects.all()
    form = PhoneDIDForm
    

class PhoneDIDDeleteView(generic.ObjectDeleteView):
    '''
    deletes a DID instance
    '''
    queryset = PhoneDID.objects.all()


class PhoneDIDDetailView(PermissionRequiredMixin, generic.ObjectView):
    '''
    returns the DID detail page with context
    '''
    
    queryset = PhoneDID.objects.all()
    permission_required=get_permission_for_model(PhoneDID, "view")

    def get_extra_context(self, request, instance):
        context: dict = {}

        context['start'] = format_number_flag(instance.start)
        context['end'] = format_number_flag(instance.end)
        context['num_did'] = instance.get_did_count()
        try:
            context['maintainer'] = PhoneInfo.objects.filter(site=instance.delivery.site).first()
        except:
            pass
        return context


class PhoneDIDBulkImportView(generic.BulkImportView):
    queryset = PhoneDID.objects.all()
    model_form = PhoneDIDBulkImportForm

    def save_object(self, object_form, request):
        instance = object_form.save()
        
        if not instance.end or instance.end == 0:
            instance.end = instance.start
            instance.save()

        return instance

    def post(self, request):
        '''
        post request handler
        if additionnal changes is needed
        '''
        response = super().post(request)
        return response


class PhoneDIDAddSiteView(generic.ObjectEditView):
    '''
    adds a site automatically to the DID
    '''
    queryset = PhoneDID.objects.all()
    form = PhoneDIDForm

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
