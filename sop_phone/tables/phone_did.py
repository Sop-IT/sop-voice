import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable
from sop_phone.models import PhoneDID
from sop_phone.utils import format_number_flag


__all__ = (
    'PhoneDIDTable',
)


class PhoneDIDTable(NetBoxTable):
    '''
    table for all DID List
    '''
    delivery = tables.Column(
        verbose_name=_('Delivery'), linkify=True
    )
    site = tables.Column(
        verbose_name=_('Site'), linkify=True
    )
    start = tables.Column(
        verbose_name=_('Start number'), linkify=True,
    )
    end = tables.Column(
        verbose_name=_('End number'), linkify=True,
    )
    size = tables.Column(
        verbose_name="Size", accessor="start", orderable=False,
    )

    class Meta(NetBoxTable.Meta):
        model = PhoneDID
        fields = ('actions', 'pk', 'id', 'start', 'end', 'delivery', 'site', 'created', 'last_updated')
        default_columns = ('start', 'end', 'delivery', 'size')

    def render_start(self, record):
        return format_number_flag(record.start)

    def render_end(self, record):
        return format_number_flag(record.end)
    
    def render_size(self, record):
        return (record.end-record.start)+1
