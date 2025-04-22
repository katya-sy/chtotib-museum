from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe
import os

register = template.Library()


@register.simple_tag
def svg_icon(icon_name, css_class=""):
    icon_path = f"icons/{icon_name}.svg"
    path = static(icon_path)

    if not os.path.exists(path.lstrip('/')):
        return mark_safe(f'<div class="{css_class}">Иконка не найдена</div>')

    with open(path.lstrip('/'), 'r') as f:
        svg = f.read()
        if css_class:
            svg = svg.replace('<svg ', f'<svg class="{css_class}" ')
        return mark_safe(svg)
