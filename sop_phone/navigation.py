from django.utils.translation import gettext_lazy as _

from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem


menu = PluginMenu(
    label='SOP Phone',
    icon_class="mdi mdi-phone",
    groups=(
        (
            ('Phone'),
            (
                PluginMenuItem(
                    link=f'plugins:sop_phone:phoneinfo_list',
                    link_text=_('Informations'),
                    permissions=[f'sop_phone.view_phoneinfo'],
                    buttons=(
                        PluginMenuButton(
                            link=f'plugins:sop_phone:phoneinfo_add',
                            title='Add',
                            icon_class='mdi mdi-plus-thick',
                            permissions=[f'sop_phone.add_phoneinfo'],
                        ),
                    ),
                ),
                PluginMenuItem(
                    link=f'plugins:sop_phone:phonedelivery_list',
                    link_text=_('Deliveries'),
                    permissions=[f'sop_phone.view_phonedelivery'],
                    buttons=(
                        PluginMenuButton(
                            link=f'plugins:sop_phone:phonedelivery_add',
                            title='Add',
                            icon_class='mdi mdi-plus-thick',
                            permissions=[f'sop_phone.add_phonedelivery'],
                        ),
                    ),
                ),
                PluginMenuItem(
                    link=f'plugins:sop_phone:phonedid_list',
                    link_text=_('DIDs'),
                    permissions=[f'sop_phone.view_phonedid'],
                    buttons=(
                        PluginMenuButton(
                            link=f'plugins:sop_phone:phonedid_add',
                            title='Add',
                            icon_class='mdi mdi-plus-thick',
                            permissions=[f'sop_phone.add_phonedid'],
                        ),
                        PluginMenuButton(
                            link=f'plugins:sop_phone:phonedid_import',
                            title='Import',
                            icon_class='mdi mdi-upload',
                            permissions=[f'sop_phone.add_phonedid'],
                        ),
                    ),
                ),
                PluginMenuItem(
                    link=f'plugins:sop_phone:phonemaintainer_list',
                    link_text=_('Maintainers'),
                    permissions=[f'sop_phone.view_phonemaintainer'],
                    buttons=(
                        PluginMenuButton(
                            link=f'plugins:sop_phone:phonemaintainer_add',
                            title='Add',
                            icon_class='mdi mdi-plus-thick',
                            permissions=[f'sop_phone.add_phonemaintainer'],
                        ),
                        PluginMenuButton(
                            link=f'plugins:sop_phone:phonemaintainer_import',
                            title='Import',
                            icon_class='mdi mdi-upload',
                            permissions=[f'sop_phone.add_phonemaintainer'],
                        ),
                    ),
                ),
            ),
        ),
    ),
)


