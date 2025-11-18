from netbox.plugins import PluginConfig


class SopPhoneConfig(PluginConfig):
    name = "sop_phone"
    verbose_name = "SOP Phone"
    description = "Manage phone informations of each site."
    version='0.4.9'
    author = "Soprema NOC team"
    author_email = "noc@soprema.com"
    base_url = "sop-phone"
    min_version = "4.4.0"

config = SopPhoneConfig

