from django.test import TestCase
from django.urls import reverse


class ApiViewTests(TestCase):
    def test_home_returns_welcome_message(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to CSC 325!"})

    def test_about_returns_course_information(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "course": "CSC 325",
                "description": "Continuous Integration and Continuous Delivery (CI/CD).",
            },
        )
