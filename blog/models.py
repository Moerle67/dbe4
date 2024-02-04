from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(("Überschrift"), max_length=250)
    slug = models.SlugField(("Schlagwort"))
    body = models.TextField(("Inhalt"))
    
    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse("Post_detail", kwargs={"pk": self.pk})
