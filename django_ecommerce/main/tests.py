"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import RequestFactory
from main import views

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import index

class MainPageTests(TestCase):

    def test_root_resolvers_to_main_view(self):
        main_page=resolve('/')
        self.assertEqual(main_page.func,index)
