# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bootstrap3.utils import render_tag


def render_table(content=None, border=True, hover=True, striped=False):
    """
    Render a Bootstrap table
    class: .table-hover .table-bordered .table-striped .table-condensed
    """
    attrs = {
        'class': 'table{0}{1}{2}'.format(' table-bordered' if border else '',
                                         ' table-hover' if hover else '',
                                         ' table-striped' if striped else ''),
    }
    return render_tag('table', attrs=attrs, content=content)


def render_tr(content=None, theme=None):
    """
    Render a Bootstrap table - tr
    class: .active .success .info .warning .danger
    """
    attrs = {}
    if theme is not None:
        attrs['class'] = theme
    render_tag('tr', attrs=attrs, content=content)


def render_table_detail(obj, **kwargs):
    table = render_table()
