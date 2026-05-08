from netbox.api.routers import NetBoxRouter

from sop_phone.api.views import PhoneDeliveryViewSet, PhoneDIDViewSet, PhoneInfoViewSet, PhoneMaintainerViewSet


router = NetBoxRouter()

router.register('phone-deliveries', PhoneDeliveryViewSet)
router.register('phone-dids', PhoneDIDViewSet)
router.register('phone-infos', PhoneInfoViewSet)
router.register('phone-maintainers', PhoneMaintainerViewSet)

urlpatterns = router.urls
