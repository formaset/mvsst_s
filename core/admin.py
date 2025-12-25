from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Общее", {"fields": ("site_title", "organization_name", "tagline", "logo")}),
        ("Контакты", {"fields": ("phone", "email", "address")}),
        ("Контент", {"fields": ("about_title", "about_text", "mission_title", "mission_text")}),
        ("Соцсети", {"fields": ("vk", "telegram", "youtube")}),
        ("SEO", {"fields": ("seo_title", "seo_description")}),
    )

    def has_add_permission(self, request):
        # делаем "singleton": только одна запись
        if SiteSettings.objects.exists():
            return False
        return True
