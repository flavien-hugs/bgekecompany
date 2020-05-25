# -*- coding: utf-8 -*-
# app/urls.py

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from app.models import Entreprise
from app.serializers import EntrepriseSerializer


# Test la vue

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_entreprise(name="", contact="", location=""):
        if name != "" and contact != "" and location != "":
            Entreprise.objects.create(name=name, contact=contact,
                                      location=location)

    def setUp(self):
        # test de donnée                                                
        self.create_entreprise("unsta inc", "+225 00 00 00 00", "Bouaké")


class GetAllEntrepriseTest(BaseViewTest):

    def test_get_all_entreprise(self):
        response = self.client.get(
            reverse("api", kwargs={"version": "v1"})
        )
        excepted = Entreprise.objects.all()
        serialized = EntrepriseSerializer(excepted, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
