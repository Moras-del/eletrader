from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from .forms import UserForm
from .models import Profile

class UserTestCase(TestCase):


    def test_edit_user(self):
        self.user = Profile.objects.create_user(username="user", password="password")
        self.client.login(username="user", password="password")
        response = self.client.post(reverse("account:edit"), data={"phone_number": "123456789", "email": "email@domain.pl"})
        user = Profile.objects.all()[0]
        self.assertEquals(user.email, "email@domain.pl")
        self.assertEquals(user.phone_number, "123456789")
        self.assertURLEqual(response.url, "/account/")

    def test_register_user(self):
        self.client.post(reverse("account:register"),
                                    data={"username": "username", "email": "email@domain.pl", "password": "password", "confirm_password": "password"})
        user = Profile.objects.all()[0]
        self.assertEquals(user.username, "username")


class FormTestCase(TestCase):

    def test_register_user(self):
        form_data = {"username": "username", "email": "email@domain.pl", "password": "password", "confirm_password": "password"}
        form = UserForm(form_data)
        is_valid = form.is_valid()
        self.assertTrue(is_valid)

    def test_register_user_false(self):
        form_data = {"username": "username", "email": "email@domain.pl", "password": "password", "confirm_password": "WRONG_PASSWORD"}
        form = UserForm(form_data)
        is_valid = form.is_valid()
        self.assertFalse(is_valid)






