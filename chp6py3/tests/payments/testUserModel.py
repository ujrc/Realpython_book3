from django.test import TestCase, SimpleTestCase
from payments.models import User
from django.db import IntegrityError

class UserModelTest(TestCase):
    @classmethod
    #def setUpTestDate(cls):
    def setUpClass(cls):
        super(UserModelTest,cls).setUpClass()
        cls.test_user=User(email='j@j.com', name='test user')
        cls.test_user.save()

    def test_user_to_string_print_email(self):
        self.assertEquals(str(self.test_user),'j@j.com')

    def test_get_by_id(self):
        self.assertEquals(User.get_by_id(1),self.test_user)

    def test_create_user_function_stores_in_database(self):
        user=User.create('test','test@t.com','tt','1234','22')
        self.assertEquals(User.objects.get(email='test@t.com'),user)

    def test_create_user_already_exists_trhows_IntegrityError(self):
        self.assertRaises(IntegrityError,
        User.create,
        'test user',
        'j@j.com',
        'jj',
        '1234',
        89)
