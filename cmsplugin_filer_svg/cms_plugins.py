# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django.templatetags.static import static
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import FilerSVG
from .forms import FilerSVGForm

class FilerSVGPlugin(CMSPluginBase):
    module = _('Filer')
    name = _('SVG')
    model = FilerSVG
    form = FilerSVGForm
    text_enabled = True
    admin_preview = False
    raw_id_fields = ('image', 'page_link')
    render_template = 'svg.html'

    fieldsets = (
        (None, {
            'fields': [
                'image',
                'image_url',
            ]
        }),
        (_('More'), {
            'classes': ('collapse',),
            'fields': (
                'free_link',
                'page_link',
                'file_link',
                ('original_link', 'target_blank',),
                'image_classes',
                'link_attributes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(FilerSVGPlugin, self).render(context, instance, placeholder)
        context['link'] = instance.link
        return context

    def icon_src(self, instance):
        return static('filer_svg/img/image.png')

    def icon_alt(self, instance):
        return '%s - %s' % (force_text(self.name), instance.image.url if instance.image else instance.link)

plugin_pool.register_plugin(FilerSVGPlugin)
