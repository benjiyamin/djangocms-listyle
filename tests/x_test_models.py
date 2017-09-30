# -*- coding: utf-8 -*-
from django.test import TestCase

from djangocms_listyle.models import ListStyle, UL, OL


class ListStyleTestCase(TestCase):

    def setUp(self):
        ListStyle.objects.create(
            list_type=UL
        )
        ListStyle.objects.create(
            list_type=OL
        )

    def test_unordered_instance(self):
        """Unordered ListStyle instance has been created"""
        style = ListStyle.objects.get(tag_type='ul')
        self.assertEqual(style.list_type, 'ul')

    def test_ordered_instance(self):
        """Order ListStyle instance has been created"""
        style = ListStyle.objects.get(tag_type='ol')
        self.assertEqual(style.list_type, 'ol')
