from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Character


class CharacterAccessTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user('lectora')
        cls.published = Character.objects.create(
            slug='publicado', name='Publicado', description='x', author=cls.user,
            status=Character.Status.PUBLISHED,
        )
        cls.draft = Character.objects.create(
            slug='borrador', name='Borrador', description='x', author=cls.user,
        )

    def test_anonymous_is_sent_to_login(self):
        for url in (reverse('characters:list'), self.published.get_absolute_url()):
            response = self.client.get(url)
            self.assertRedirects(response, f"{reverse('accounts:login')}?next={url}")

    def test_logged_in_sees_only_published(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('characters:list'))
        self.assertContains(response, 'Publicado')
        self.assertNotContains(response, 'Borrador')
        self.assertEqual(self.client.get(self.published.get_absolute_url()).status_code, 200)
        self.assertEqual(self.client.get(self.draft.get_absolute_url()).status_code, 404)
