from netbox.api.viewsets import NetBoxModelViewSet
from netbox.api.metadata import ContentTypeMetadata

from sop_phone.models import PhoneDelivery, PhoneDID, PhoneInfo, PhoneMaintainer
from sop_phone.filtersets import PhoneDeliveryFilterSet, PhoneDIDFilterSet, PhoneInfoFilterSet, PhoneMaintainerFilterSet
from sop_phone.api.serializers import PhoneDeliverySerializer, PhoneDIDSerializer, PhoneInfoSerializer, PhoneMaintainerSerializer 


__all__ = (
    'PhoneDeliveryViewSet',
    'PhoneDIDViewSet',
    'PhoneInfoViewSet',
    'PhoneMaintainerViewSet',
)

class PhoneMaintainerViewSet(NetBoxModelViewSet):
    metadata_class = ContentTypeMetadata
    queryset = PhoneMaintainer.objects.all().order_by("pk")
    serializer_class = PhoneMaintainerSerializer
    filterset_class = PhoneMaintainerFilterSet


class PhoneInfoViewSet(NetBoxModelViewSet):
    metadata_class = ContentTypeMetadata
    queryset = PhoneInfo.objects.all().order_by("pk")
    serializer_class = PhoneInfoSerializer
    filterset_class = PhoneInfoFilterSet


class PhoneDIDViewSet(NetBoxModelViewSet):
    metadata_class = ContentTypeMetadata
    queryset = PhoneDID.objects.all().order_by("pk")
    serializer_class = PhoneDIDSerializer
    filterset_class = PhoneDIDFilterSet


class PhoneDeliveryViewSet(NetBoxModelViewSet):
    metadata_class = ContentTypeMetadata
    queryset = PhoneDelivery.objects.all().order_by("pk")
    serializer_class = PhoneDeliverySerializer
    filterset_class = PhoneDeliveryFilterSet
