from django.conf import settings
from django.db import models
from django.urls import reverse


class Character(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Borrador'
        PUBLISHED = 'published', 'Publicado'

    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    lore = models.TextField(blank=True)
    image = models.ImageField(upload_to='characters/', blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='characters',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('characters:detail', kwargs={'slug': self.slug})
