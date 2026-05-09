from django.shortcuts import get_object_or_404

from netbox.views import generic
from dcim.models import Site

from sop_phone.forms.phone_info import PhoneInfoForm, PhoneInfoFilterForm, PhoneInfoBulkEditForm
from sop_phone.models import PhoneInfo
from sop_phone.filtersets import PhoneInfoFilterSet
from sop_phone.tables.phone_info import PhoneInfoTable


__all__ = (
    'PhoneInfoEditView',
    'PhoneInfoDeleteView',
    'PhoneInfoDetailView',
    'PhoneInfoListView',
    'PhoneInfoBulkEditView',
    'PhoneInfoBulkDeleteView',
    'PhoneInfoAddView',
)


class PhoneInfoAddView(generic.ObjectEditView):
    queryset = PhoneInfo.objects.all()
    form = PhoneInfoForm

    def get_object(self, **kwargs):
        '''
        if pk in kwargs, this the request is from "phone" site tab view
        so pk is the site id
        '''
        if 'pk' in kwargs:
            return self.queryset.model(site=get_object_or_404(Site, pk=kwargs['pk']))
        return self.queryset.model()

    def alter_object(self, obj, request, args, kwargs):
        '''
        '''
        if 'pk' in kwargs:
            pk = kwargs.get('pk')
            site = get_object_or_404(Site, pk=pk)
            obj = self.queryset.model
            return obj(site=site)
        return obj

    def get(self, request, *args, **kwargs):
        '''
        get request handler
        '''
        response = super().get(request, *args, **kwargs)
        return response


class PhoneInfoListView(generic.ObjectListView):
    queryset = PhoneInfo.objects.all()
    table = PhoneInfoTable
    filterset = PhoneInfoFilterSet
    filterset_form = PhoneInfoFilterForm


class PhoneInfoDetailView(generic.ObjectView):
    queryset = PhoneInfo.objects.all()
    
    def get_extra_context(self, request, instance:PhoneInfo) -> dict:
        context:dict = {}
        context['num_del'] = instance.get_del_count()
        context['num_did'] = instance.get_did_count()
        return context


class PhoneInfoEditView(generic.ObjectEditView):
    queryset = PhoneInfo.objects.all()
    form = PhoneInfoForm

    def get_return_url(self, request, obj=None):
        try:
            return '/dcim/sites/' + str(obj.site.pk) + '/phone/'
        except:
            return '/dcim/sites/'


class PhoneInfoDeleteView(generic.ObjectDeleteView):
    queryset = PhoneInfo.objects.all()

    def get_return_url(self, request, obj=None) -> str:
        try:
            if obj is None:
                raise Exception
            return f'/dcim/sites/{obj.site.pk}/phone'
        except:
            return '/dcim/sites/'


class PhoneInfoBulkEditView(generic.BulkEditView):
    queryset = PhoneInfo.objects.all()
    table = PhoneInfoTable
    form = PhoneInfoBulkEditForm
    filterset = PhoneInfoFilterSet


class PhoneInfoBulkDeleteView(generic.BulkDeleteView):
    queryset = PhoneInfo.objects.all()
    table = PhoneInfoTable
    filterset = PhoneInfoFilterSet
