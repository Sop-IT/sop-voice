
from utilities.views import GetRelatedModelsMixin, register_model_view

from netbox.views import generic

from dcim.models import Site

from sop_phone.models import PhoneMaintainer, PhoneInfo, PhoneDID
from sop_phone.filtersets import PhoneMaintainerFilterSet
from sop_phone.tables.phone_maintainer import PhoneMaintainerTable
from sop_phone.forms.phone_maintainer import PhoneMaintainerForm, PhoneMaintainerFilterForm, PhoneMaintainerBulkEditForm, PhoneMaintainerBulkImportForm



__all__ = (
    'PhoneMaintainerView',
    'PhoneMaintainerEditView',
    'PhoneMaintainerDeleteView',
    'PhoneMaintainerBulkEditView',
    'PhoneMaintainerBulkDeleteView',
    'PhoneMaintainerBulkImportView',
    'PhoneMaintainerContactsView'
)


class PhoneMaintainerListView(generic.ObjectListView):
    queryset = PhoneMaintainer.objects.all()
    table = PhoneMaintainerTable
    filterset = PhoneMaintainerFilterSet
    filterset_form = PhoneMaintainerFilterForm


class PhoneMaintainerView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = PhoneMaintainer.objects.all()

    def get_format(self, values) -> str | None:
        qs = [str(item['site__id']) for item in values]
        if qs == []:
            return None
        return f'id=' + '&id='.join(qs)

    def get_extra_context(self, request, instance:PhoneMaintainer):
        '''
        additionnal context for the related models/objects
        as they are not directly related
        '''
        context: dict = {}

        sites = PhoneInfo.objects.filter(maintainer=instance)
        site_ids = sites.values('site__id')

        context['num_did'] = instance.get_did_count()
        context['site_ids'] = site_ids
        context['related_models'] = self.get_related_models(
            request, 
            instance, 
            extra=(
                (Site.objects.filter(
                    pk__in=site_ids
                ), 'id'),
                (PhoneDID.objects.filter(
                    delivery__site__in=site_ids
                ), 'maintainer_id')
            )
        )
        context['site'] = Site
        context['restricted'] = self.get_format(site_ids)
        return context


class PhoneMaintainerEditView(generic.ObjectEditView):
    '''
    edits a maintainer instance
    '''
    queryset = PhoneMaintainer.objects.all()
    form = PhoneMaintainerForm


class PhoneMaintainerDeleteView(generic.ObjectDeleteView):
    '''
    deletes a maintainer instance
    '''
    queryset = PhoneMaintainer.objects.all()


class PhoneMaintainerBulkDeleteView(generic.BulkDeleteView):
    '''
    deletes multiple phone maintainers instances
    '''
    queryset = PhoneMaintainer.objects.all()
    table = PhoneMaintainerTable
    filterset = PhoneMaintainerFilterSet


class PhoneMaintainerBulkEditView(generic.BulkEditView):
    '''
    edits multiple phone maintainer instances
    '''
    queryset = PhoneMaintainer.objects.all()
    table = PhoneMaintainerTable
    form = PhoneMaintainerBulkEditForm
    filterset = PhoneMaintainerFilterSet


class PhoneMaintainerBulkImportView(generic.BulkImportView):
    queryset = PhoneMaintainer.objects.all()
    model_form = PhoneMaintainerBulkImportForm

    def save_object(self, object_form, request):
        instance = object_form.save()
        return instance

    def post(self, request):
        '''
        post request handler
        if additionnal changes is needed
        '''
        response = super().post(request)
        return response


@register_model_view(PhoneMaintainer, 'contacts')
class PhoneMaintainerContactsView(generic.ObjectContactsView):
    queryset = PhoneMaintainer.objects.all()

