from django.contrib import admin
from .models import ContentPage, ContentSection, KeyFact, LeadershipMember, PerformanceItem, SiteSettings

admin.site.site_header = "АНО «МосводостокСтройТрест»"
admin.site.site_title = "Администрирование сайта"
admin.site.index_title = "Управление контентом"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Общее", {"fields": ("site_title", "organization_name", "tagline", "logo")}),
        ("Главная", {"fields": ("hero_title", "hero_subtitle", "hero_image", "home_about_title", "home_about_text")}),
        ("Контакты", {"fields": ("phone", "email", "address", "contacts_title", "contacts_intro", "contacts_map_embed")}),
        ("Миссия", {"fields": ("mission_title", "mission_text")}),
        ("SEO", {"fields": ("seo_title", "seo_description")}),
    )

    def has_add_permission(self, request):
        # делаем "singleton": только одна запись
        if SiteSettings.objects.exists():
            return False
        return True


@admin.register(ContentPage)
class ContentPageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    list_filter = ("slug",)
    search_fields = ("title", "lead", "body")


class ContentSectionInline(admin.StackedInline):
    model = ContentSection
    extra = 0
    fields = ("title", "body", "image", "button_text", "button_url", "style", "order")
    ordering = ("order",)


ContentPageAdmin.inlines = [ContentSectionInline]


@admin.register(KeyFact)
class KeyFactAdmin(admin.ModelAdmin):
    list_display = ("value", "title", "order")
    list_editable = ("order",)
    search_fields = ("title", "value")


@admin.register(LeadershipMember)
class LeadershipMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "order")
    list_editable = ("order",)
    search_fields = ("name", "position")


@admin.register(PerformanceItem)
class PerformanceItemAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "order")
    list_editable = ("order",)
    list_filter = ("date",)
    search_fields = ("title", "description")
