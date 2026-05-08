from netbox.search import SearchIndex, register_search

from sop_phone.models import PhoneDID, PhoneDelivery, PhoneMaintainer


@register_search
class PhoneDIDSearchIndex(SearchIndex):
    model = PhoneDID
    fields = (
        ('start', 100),
        ('end', 100),
    )


@register_search
class PhoneDeliverySearchIndex(SearchIndex):
    model = PhoneDelivery
    fields = (
        ('delivery', 100),
        ('provider', 100),
        ('site', 500),
    )


@register_search
class PhoneMaintainerSearchIndex(SearchIndex):
    model = PhoneMaintainer
    fields = (
        ('name', 100),
        ('slug', 100),
        ('description', 500),
        ('comments', 1000),
        ('status', 1000),
    )
