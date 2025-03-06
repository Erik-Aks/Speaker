from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=False)
    content = models.TextField(blank=False, default="")
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)  # Przechowuje obrazy w folderze "media".
    created_at = models.DateTimeField(auto_now_add=True)  # Ustawia czas utworzenia
    updated_at = models.DateTimeField(auto_now=True)  # Aktualizuje się automatycznie przy zapisie

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        if self.year:
            return "{} ({})".format(self.title, self.year)
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Artikuły"
