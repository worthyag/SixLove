from django.test import TestCase
from django.urls import reverse

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
