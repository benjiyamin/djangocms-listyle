
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from djangocms_style.cms_plugins import StylePlugin

from . import models


class ListStylePlugin(StylePlugin):
    model = models.ListStyle
    name = 'List'
    render_template = 'djangocms_listyle/index.html'

    fieldsets = (
        (None, {
            'fields': (
                'label',
                'list_type',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'additional_classes',
                'id_name',
                'template',
                'attributes',
            ),
        }),
        (_('Inline style settings'), {
            'classes': ('collapse',),
            'fields': (
                ('padding_top', 'padding_right',
                 'padding_bottom', 'padding_left'),
                ('margin_top', 'margin_right',
                 'margin_bottom', 'margin_left'),
            ),
        }),
    )

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_listyle/index.html'.format(instance.template)


plugin_pool.register_plugin(ListStylePlugin)
