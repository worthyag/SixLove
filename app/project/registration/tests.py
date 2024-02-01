from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model

# Create your tests here.


class RegistrationViewsTests(TestCase):
    """
    Testing the registration views work as expected.
    """

    def registration_view_uses_template(self, url_name: str, template: str):
        """
        Helper function to minimise code repetition.

        Parameters
        ----------
        url_name : str
          The name associated with the url (assigned in the views file).
        template : str
          The name of the template.

        Notes
        -----
        The template parameter requires only the primary domain, e.g: 'index' 
        rather than './registration/index.html
        """
        # Getting the url for the chosen view
        url = reverse(url_name)

        # Sending a GET response to the chosen view.
        response = self.client.get(url)

        # Checking whether the chosen view uses the template.
        self.assertTemplateUsed(
            response,
            f"./registration/{template}.html"
        )

    def test_home_view_uses_template(self):
        """
        Testing the the home view uses the given template.
        """
        # Checking whether the home view uses the template.
        self.registration_view_uses_template("home", "index")

    def test_user_login_view_uses_template(self):
        """
        Testing the the user_login view uses the given template.
        """
        # Checking whether the home view uses the template.
        self.registration_view_uses_template("login", "login")

    def test_signup_view_uses_template(self):
        """
        Testing the the signup view uses the given template.
        """
        # Checking whether the home view uses the template.
        self.registration_view_uses_template("signup", "signup")

    def test_onboarding_view_uses_template(self):
        """
        Testing the the onboarding view uses the given template.
        """
        # Checking whether the home view uses the template.
        self.registration_view_uses_template("onboarding", "onboarding")


class RegistrationUserAuthenticationTests(TestCase):
    """
    Testing the user authentication mechanism works as expected.
    """

    def setUp(self):
        """Creating a user to test."""

        self.user_data = {
            "first_name": "test",
            "last_name": "user",
            "email": "testuser@email.com",
            "username": "test_user",
            "password": "password1"
        }

        self.user = get_user_model().objects.create_user(**self.user_data)

    def create_login_response(self):
        """Helper function to minimise code repetition."""
        response = self.client.post(reverse("login"), {
            "username": self.user_data["username"],
            "password": self.user_data["password"],
        })

        return response

    def test_existing_user_can_login(self):
        """"""
        response = self.create_login_response()
        # Checking that login is successful.
        self.assertEqual(response.status_code, 302)

    def test_existing_user_is_redirected_logged_in(self):
        """"""
        response = self.create_login_response()
        # Checking that the user is redirected to the home page once logged in.
        self.assertRedirects(response, reverse("home"))

    def test_existing_user_is_authenticated(self):
        """"""
        # Logging the user in.
        self.create_login_response()

        # Checking that the user is authenticated
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_existing_user_can_logout(self):
        """"""
        # Logging the user in.
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        # Logging the user out + checking whether the operation was successfully.
        response = self.client.post(reverse("logout"), follow=True)
        # self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    # def test_new_user_can_signup(self):
    #     pass
