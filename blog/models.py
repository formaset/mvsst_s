from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Черновик"
        PUBLISHED = "published", "Опубликовано"

    title = models.CharField("Заголовок", max_length=250)
    slug = models.SlugField("Slug", max_length=255, unique=True)
    excerpt = models.TextField("Краткое описание", blank=True, default="")
    cover = models.ImageField("Обложка", upload_to="blog/", blank=True, null=True)

    content = RichTextField("Текст", blank=True, default="")

    status = models.CharField("Статус", max_length=20, choices=Status.choices, default=Status.DRAFT)
    published_at = models.DateTimeField("Дата публикации", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-published_at", "-created_at"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
