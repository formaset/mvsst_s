from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class SiteSettings(models.Model):
    site_title = models.CharField("Название сайта", max_length=200, default="МВС СТ")
    organization_name = models.CharField("Название организации", max_length=200, blank=True, default="МВС СТ")
    tagline = models.CharField("Слоган", max_length=250, blank=True, default="")

    logo = models.ImageField("Логотип (PNG/SVG как картинка)", upload_to="site/", blank=True, null=True)
    phone = models.CharField("Телефон", max_length=100, blank=True, default="")
    email = models.EmailField("Email", blank=True, default="")
    address = models.CharField("Адрес", max_length=300, blank=True, default="")

    hero_title = models.CharField("Главная: заголовок", max_length=200, blank=True, default="")
    hero_subtitle = models.TextField("Главная: подзаголовок", blank=True, default="")
    hero_image = models.ImageField("Главная: фоновое изображение", upload_to="site/", blank=True, null=True)

    home_about_title = models.CharField("Главная: блок об организации", max_length=200, blank=True, default="Об организации")
    home_about_text = CKEditor5Field("Главная: текст об организации", blank=True, default="")

    mission_title = models.CharField("Заголовок 'Миссия'", max_length=200, blank=True, default="Миссия")
    mission_text = CKEditor5Field("Текст 'Миссия'", blank=True, default="")

    contacts_title = models.CharField("Контакты: заголовок", max_length=200, blank=True, default="Контакты")
    contacts_intro = models.TextField("Контакты: вводный текст", blank=True, default="")
    contacts_map_embed = models.TextField("Контакты: код карты (iframe)", blank=True, default="")

    seo_title = models.CharField("SEO title", max_length=255, blank=True, default="")
    seo_description = models.CharField("SEO description", max_length=300, blank=True, default="")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self) -> str:
        return "Настройки сайта (SiteSettings)"


class ContentPage(models.Model):
    class Slugs(models.TextChoices):
        ORGANIZATION_ABOUT = "organization-about", "Об организации"
        ORGANIZATION_KEY_FACTS = "organization-key-facts", "Ключевые факты"
        ORGANIZATION_LEADERSHIP = "organization-leadership", "Руководство"
        ORGANIZATION_PERFORMANCE = "organization-performance", "Оценка деятельности"
        CAREER = "career", "Карьера"

    slug = models.SlugField("Slug", max_length=200, unique=True, choices=Slugs.choices)
    title = models.CharField("Заголовок", max_length=200)
    lead = models.TextField("Лид", blank=True, default="")
    body = CKEditor5Field("Контент", blank=True, default="")

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)


class KeyFact(models.Model):
    title = models.CharField("Подпись", max_length=200)
    value = models.CharField("Значение", max_length=120)
    description = models.CharField("Описание", max_length=200, blank=True, default="")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Ключевой факт"
        verbose_name_plural = "Ключевые факты"
        ordering = ["order"]

    def __str__(self) -> str:
        return f"{self.value} — {self.title}"


class LeadershipMember(models.Model):
    name = models.CharField("ФИО", max_length=200)
    position = models.CharField("Должность", max_length=200)
    photo = models.ImageField("Фото", upload_to="leadership/", blank=True, null=True)
    bio = CKEditor5Field("Биография", blank=True, default="")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководство"
        ordering = ["order", "name"]

    def __str__(self) -> str:
        return self.name


class PerformanceItem(models.Model):
    title = models.CharField("Название", max_length=200)
    date = models.DateField("Дата", blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="performance/", blank=True, null=True)
    description = models.TextField("Описание", blank=True, default="")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Оценка деятельности"
        verbose_name_plural = "Оценка деятельности"
        ordering = ["order", "-date"]

    def __str__(self) -> str:
        return self.title
