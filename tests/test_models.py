
from django.test import TestCase

from djangocms_listyle.models import ListStyle, UL, OL


class ListStyleTestCase(TestCase):

    def setUp(self):
        self.listyle = ListStyle.objects.create()

    def test_listyle_instance(self):
        """List Style has been created"""
        listyle = ListStyle.objects.get()
        self.assertEqual(self.listyle, listyle)


class ListStyleTestCase2(TestCase):

    def setUp(self):
        ListStyle.objects.create(
            list_type=UL
        )
        ListStyle.objects.create(
            list_type=OL
        )

    def test_unordered_instance(self):
        """Unordered ListStyle instance has been created"""
        style = ListStyle.objects.get(list_type='ul')
        self.assertEqual(style.list_type, 'ul')

    def test_ordered_instance(self):
        """Order ListStyle instance has been created"""
        style = ListStyle.objects.get(list_type='ol')
        self.assertEqual(style.list_type, 'ol')
