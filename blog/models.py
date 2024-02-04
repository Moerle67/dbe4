from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(("Überschrift"), max_length=250)
    slug = models.SlugField(("Schlagwort"))
    body = models.TextField(("Inhalt"))
    publish = models.DateTimeField(("veröffentlicht"), default=timezone.now)
    created = models.DateTimeField(("erstellt"), auto_now_add=True)
    updated = models.DateTimeField(("angepasst"), auto_now=True)
    status = models.CharField(("Status"), max_length=2, 
                                    choices=Status.choices,
                                    default=Status.DRAFT)
    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse("Post_detail", kwargs={"pk": self.pk})
