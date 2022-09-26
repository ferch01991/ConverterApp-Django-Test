from django.test import TestCase, Client
from django.urls import reverse

class testLengthConversion(TestCase):
    """
    This class conteins test that convert measurements from 
    one unit of measurement to another
    """

    def setUp(self):
        """
        This method run before the execution of each test case
        """
        self.client = Client()
        self.url = reverse("length:convert")

    def test_centimeter_to_meter_conversion(self):
        """
        Test conversion of centimeter measurement to meter
        """

        data = {
            "input_unit": "centimeter",
            "output_unit": "meter",
            "input_value": round(8096.894, 3)
        }

        response = self.client.get(self.url, data)
        self.assertContains(response, 80.969)
    
    def test_centimeter_to_mile_conversion(self):
        """
        Test conversion of centimeter measurement to mile
        """

        data = {
            "input_unit": "centimeter",
            "output_unit": "mile",
            "input_value": round(985805791.3527409, 3)
        }

        response = self.client.get(self.url, data)
        self.assertContains(response, 6125.511)

