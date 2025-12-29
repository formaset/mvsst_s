from django.apps import apps
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_news_editor_group(sender, **kwargs):
    if sender.name != "core":
        return

    permissions = Permission.objects.filter(content_type__app_label="blog", content_type__model="post")
    group, _ = Group.objects.get_or_create(name="Редактор новостей")
    group.permissions.set(permissions)

    content_page_model = apps.get_model("core", "ContentPage")
    site_settings_model = apps.get_model("core", "SiteSettings")
    default_pages = [
        ("organization-about", "Об организации"),
        ("organization-key-facts", "Ключевые факты"),
        ("organization-leadership", "Руководство"),
        ("organization-performance", "Оценка деятельности"),
        ("career", "Карьера"),
    ]
    for slug, title in default_pages:
        content_page_model.objects.get_or_create(
            slug=slug,
            defaults={"title": title, "lead": "", "body": ""},
        )

    site_settings_model.objects.get_or_create(
        id=1,
        defaults={
            "site_title": "АНО «МосводостокСтройТрест»",
            "organization_name": "АНО «МосводостокСтройТрест»",
            "tagline": "Эксплуатация и развитие водоотводящих систем города",
            "hero_title": "Инженерные решения для водоотведения Москвы",
            "hero_subtitle": "Стабильная работа инфраструктуры, прозрачная отчётность и развитие городской среды.",
            "home_about_title": "Об организации",
            "mission_title": "Миссия",
            "contacts_title": "Контакты",
        },
    )
