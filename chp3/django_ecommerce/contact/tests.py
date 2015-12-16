"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
from django.test import TestCase
from django.test import RequestFactory
from django.core.urlresolvers import resolve
from contact.views import contact
from django.shortcuts import render_to_response
import mock # used instead of database

class ContactPageTests(TestCase):

            # SetUp
        #*************#

    @classmethod
    def setUpClass(cls):
        request_factory=RequestFactory()
        cls.request=request_factory.get('/contact/')
        cls.request.session={}

        #Testing routes
        #***************#
    def test_root_resolvers_to_contact_view(self):
        contact_page=resolve('/contact/')
        self.assertEqual(contact_page.func, contact)

    def test_returns_appropriate_contact_html_response_code(self):
        resp=contact(self.request)
        self.assertEquals(resp.status_code,200)
