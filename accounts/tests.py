from django.test import TestCase
from django.urls import reverse

from characters.models import Character

from .models import User


class SignupTests(TestCase):
    def test_signup_creates_user_and_logs_in(self):
        response = self.client.post(reverse('accounts:signup'), {
            'username': 'autora',
            'password1': 'clave-larga-7391',
            'password2': 'clave-larga-7391',
        })
        self.assertRedirects(response, reverse('accounts:profile'))
        user = User.objects.get(username='autora')
        self.assertFalse(user.is_staff)
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)

    def test_signup_rejects_mismatched_passwords(self):
        response = self.client.post(reverse('accounts:signup'), {
            'username': 'autora',
            'password1': 'clave-larga-7391',
            'password2': 'otra-clave-7391',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.exists())

    def test_signup_redirects_authenticated_user(self):
        self.client.force_login(User.objects.create_user('autora'))
        response = self.client.get(reverse('accounts:signup'))
        self.assertRedirects(response, reverse('accounts:profile'))


class LoginLogoutTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('autora', password='clave-larga-7391')

    def test_login(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'autora',
            'password': 'clave-larga-7391',
        })
        self.assertRedirects(response, reverse('accounts:profile'))

    def test_login_wrong_password(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'autora',
            'password': 'incorrecta',
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_logout_requires_post(self):
        self.client.force_login(self.user)
        self.assertEqual(self.client.get(reverse('accounts:logout')).status_code, 405)
        response = self.client.post(reverse('accounts:logout'))
        self.assertRedirects(response, reverse('characters:list'), fetch_redirect_response=False)
        self.assertNotIn('_auth_user_id', self.client.session)


class ProfileTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('autora')
        cls.other = User.objects.create_user('otro')
        Character.objects.create(
            slug='mio-borrador', name='Mío borrador', description='x', author=cls.user,
        )
        Character.objects.create(
            slug='mio-publicado', name='Mío publicado', description='x', author=cls.user,
            status=Character.Status.PUBLISHED,
        )
        Character.objects.create(
            slug='ajeno', name='Ajeno', description='x', author=cls.other,
        )

    def test_profile_requires_login(self):
        url = reverse('accounts:profile')
        response = self.client.get(url)
        self.assertRedirects(response, f"{reverse('accounts:login')}?next={url}")

    def test_profile_lists_only_own_characters(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('accounts:profile'))
        self.assertContains(response, 'Mío borrador')
        self.assertContains(response, 'Mío publicado')
        self.assertNotContains(response, 'Ajeno')
        # El borrador no tiene página pública, así que no se enlaza
        self.assertContains(response, '/personajes/mio-publicado/')
        self.assertNotContains(response, '/personajes/mio-borrador/')
