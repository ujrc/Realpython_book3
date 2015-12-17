"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import ContactForm
from datetime import datetime, timedelta
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


class UserModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        ContactForm(email="a@b.com", name="Ab").save()
        ContactForm(email='test@model.com', name='Test').save()
        cls.firstUser=ContactForm(
        name='One',
        email='one@b.com',
        timestamp=datetime.today()+timedelta(days=3)
        )
        cls.firstUser.save()

    def test_contactform_str_returns_email(self):
        self.assertEquals('one@b.com',str(self.firstUser))

    def test_ordering(self):
        contacts=ContactForm.objects.all()
        self.assertEquals(self.firstUser,contacts[0])
