from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomPageTest(SimpleTestCase):
    def test_url_exist_at_correct_location_HomePageView(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")
