
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from djangocms_style.models import Style

OL = 'ol'
UL = 'ul'
LIST_TYPE_CHOICES = (
    (OL, 'Ordered'),
    (UL, 'Unordered'),
)


@python_2_unicode_compatible
class ListStyle(Style):
    list_type = models.CharField(
        max_length=2,
        choices=LIST_TYPE_CHOICES,
        default=UL,
    )

    def get_short_description(self):
        # display format:
        # Style label <tag> .list.of.classes #id
        display = []
        classes = []

        if self.label:
            display.append(self.label)
        if self.list_type:
            display.append('<{0}>'.format(self.list_type))
        if self.additional_classes:
            classes.extend(x.strip() for x in self.additional_classes.split(',') if x.strip())
        display.append('.{0}'.format('.'.join(classes)))
        if self.id_name:
            display.append('#{0}'.format(self.id_name))
        return ' '.join(display)
