import re
import phonenumbers

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from sop_phone.utils import format_number_error

__all__ = (
    'PhoneValidator',
    'PhoneMaintainerValidator',
)


class PhoneMaintainerValidator:

    @staticmethod
    def check_address(address, name:str) -> None:
        if not address:
            return
        if address.strip() == '':
            return
        if not re.match("^([^\n]* \r?\n)+[^\n]+$", address):
            raise ValidationError({
                f'{name}': _("Address must be multiline and each line must end with a space.")
            })


class PhoneValidator:

    @staticmethod
    def check_site(site) -> None:
        if site is None:
            raise ValidationError({
                'site': _("Site must be set.")
            })

    @staticmethod
    def check_delivery_site(delivery, site) -> None:
        if delivery and site and delivery.site != site:
            raise ValidationError({
                'delivery': _("{site}: Delivery must be set to the same site as the DID.")
            })

    @staticmethod
    def check_delivery_overlaps(delivery, start:int, end:int) -> None:
        if not delivery:
            return
        lstart = len(str(start))
        if len(str(delivery.dto)) == lstart:
            if start <= delivery.dto and end >= delivery.dto:
                raise ValidationError({
                    'start': _(f'{delivery.site}: This range {format_number_error(start)} -> {format_number_error(end)}\
 overlaps its own delivery DTO.')
                })

    @staticmethod
    def check_number(where:str, number:int) -> None:
        if number is None or number <= 0 :
            raise ValidationError({
                f'{where}': _("Number must be set in E164 format.")
            })
        try:
            if not phonenumbers.parse(f'+{number}'):
                raise ValidationError({
                    f'{where}': _("Number must be a valid phone number written in E164 format.")
                })
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError({
                f'{where}': _('Number must be a valid phone number written in E164 format')
                })

    @staticmethod
    def check_start_end(start:int, end:int) -> None:
        if start is None or end is None:
            return
        if len(str(start))!=len(str(end)):
            raise ValidationError({
                'end': _("End number must be the same length as start number.")
            })
        if start > end:
            raise ValidationError({
                'end': _("End number must be greater than or equal to the start number.")
            })


