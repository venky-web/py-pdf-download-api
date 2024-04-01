""""
    Helper functions
"""
import json

from api import models

def get_widgets_from_page(page):
    """ Returns list of widgets based on page definition"""

    if not page.definition:
        return []
    
    page_definition = json.loads(page.definition)
    widgets = page_definition['widgets']
    for x in widgets:
        widget = models.Widget.objects.get(widget_id=x['widgetId'])
        print(widget)

    return []

def get_widget(widget_id):
    """
        Returns widget based on widget_id
    """

    if not widget_id:
        return None
    try:
        widget = models.Widget.objects.get(widget_id=widget_id)
        if widget.definition:
            widget.definition = json.loads(widget.definition)

        return widget
    except:
        return None