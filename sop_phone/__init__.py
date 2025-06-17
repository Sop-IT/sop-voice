from netbox.plugins import PluginConfig


class SopPhoneConfig(PluginConfig):
    name = "sop_phone"
    verbose_name = "SOP Phone"
    description = "Manage phone informations of each site."
    version='0.4.6'
    author = "Leorevoir"
    author_email = "leoquinzler@epitech.eu"
    base_url = "sop-phone"
    min_version = "4.3.0"

config = SopPhoneConfig

