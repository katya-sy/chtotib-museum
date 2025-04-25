from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe
import os

register = template.Library()


@register.simple_tag
def svg_icon(icon_url, css_class=""):
    icon_path = os.path.join(settings.MEDIA_ROOT, icon_url.replace('/media/', '', 1))

    if not os.path.exists(icon_path):
        return mark_safe(f'<div class="{css_class}">Иконка не найдена</div>')

    with open(icon_path, 'r') as f:
        svg = f.read()
        if css_class:
            svg = svg.replace('<svg ', f'<svg class="{css_class}" ')
        return mark_safe(svg)
