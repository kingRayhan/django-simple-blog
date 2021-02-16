from django.db import models
from django.db.models.lookups import IsNull
from django_editorjs import EditorJsField
from autoslug import AutoSlugField


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=220)
    # slug = AutoSlugField(populate_from='title', unique_with=['pub_date'])
    slug = models.CharField(max_length=220)
    body = EditorJsField()
    excerpt = models.CharField(max_length=180, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False)
    thumbnail = models.ImageField(
        upload_to='uploads/', null=True, blank=True)
