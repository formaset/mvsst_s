from django.db import models
from ckeditor.fields import RichTextField


class SiteSettings(models.Model):
    site_title = models.CharField("Название сайта", max_length=200, default="МВС СТ")
    organization_name = models.CharField("Название организации", max_length=200, blank=True, default="МВС СТ")
    tagline = models.CharField("Слоган", max_length=250, blank=True, default="")

    logo = models.ImageField("Логотип (PNG/SVG как картинка)", upload_to="site/", blank=True, null=True)
    phone = models.CharField("Телефон", max_length=100, blank=True, default="")
    email = models.EmailField("Email", blank=True, default="")
    address = models.CharField("Адрес", max_length=300, blank=True, default="")

    about_title = models.CharField("Заголовок 'О нас'", max_length=200, blank=True, default="О нас")
    about_text = RichTextField("Текст 'О нас'", blank=True, default="")

    mission_title = models.CharField("Заголовок 'Миссия'", max_length=200, blank=True, default="Миссия")
    mission_text = RichTextField("Текст 'Миссия'", blank=True, default="")

    vk = models.URLField("VK", blank=True, default="")
    telegram = models.URLField("Telegram", blank=True, default="")
    youtube = models.URLField("YouTube", blank=True, default="")

    seo_title = models.CharField("SEO title", max_length=255, blank=True, default="")
    seo_description = models.CharField("SEO description", max_length=300, blank=True, default="")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self) -> str:
        return "Настройки сайта (SiteSettings)"
