
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from payments.models import User
from rest_framework import status
from main.models import StatusReport
from main.json_views import StatusCollection, StatusMember#status_collection
from main.serializers import StatusReportSerializer


class JsonViewTests(TestCase):

    @classmethod
    def setUpClass(cls):
        #super().setUpClass()
        cls.factory=APIRequestFactory()
        cls.test_user=User(id=2222,email='test@user.com')
        cls.test_user.save()

    @classmethod
    def tearDownClass(cls):
        cls.test_user.delete()

    @classmethod
    def setUpTestData(cls):
        cls.test_user=User(id=2222,email='test@user.com')

    def get_request(self,method='GET', authed=True):
        request_method=getattr(self.factory,method.lower())
        request=request_method("")
        if authed:
            force_authenticate(request, self.test_user)

        return request

    def test_get_collection(self):
        status =StatusReport.objects.all()
        expected_json=StatusReportSerializer(status, many=True).data

        response=StatusCollection.as_view()(self.get_request())
        self.assertEqual(expected_json, response.data)

    def test_get_collection_requires_logged_in_user(self):
        anon_request=self.get_request(method='GET', authed=False)
        response=StatusCollection.as_view()(anon_request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_member(self):
        statu=StatusReport( user=self.test_user, status="testing")
        statu.save()

        status=StatusReport.objects.get(pk=statu.id)
        expected_json=StatusReportSerializer(status).data

        response =StatusMember.as_view()(self.get_request(),pk=statu.id)
        self.assertEqual(expected_json,response.data)
        statu.delete()

    def test_delete_member(self):
        statu=StatusReport( user=self.test_user, status="testing")
        statu.save()

        response =StatusMember.as_view()(self.get_request(method="DELETE"),pk=statu.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        statu.delete()
# class dummyRequest(object):
#     def __init__(self, method):
#         self.method = method
#         self.encoding = 'utf8'
#         self.user = "root"
#         self.query_params = {}
#         self.META = {}
#
# class JsonViewTests(TestCase):
#
#     def test_get_collection(self):
#         status = StatusReport.objects.all()
#         expected_json = StatusReportSerializer(status,
#         many=True).data
#         #response = status_collection(dummyRequest('GET'))
#         response=StatusCollection.as_view()(dummyRequest("GET"))
#         self.assertEqual(expected_json, response.data)
