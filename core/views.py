from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from blog.models import Post
from .models import ContentPage, KeyFact, LeadershipMember, PerformanceItem


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["latest_posts"] = (
            Post.objects.filter(status=Post.Status.PUBLISHED)
            .order_by("-published_at", "-created_at")[:5]
        )
        ctx["key_facts"] = KeyFact.objects.all()[:4]
        return ctx


class OrganizationAboutView(TemplateView):
    template_name = "pages/organization_about.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["page"] = get_object_or_404(ContentPage, slug=ContentPage.Slugs.ORGANIZATION_ABOUT)
        return ctx


class OrganizationKeyFactsView(TemplateView):
    template_name = "pages/organization_key_facts.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["page"] = get_object_or_404(ContentPage, slug=ContentPage.Slugs.ORGANIZATION_KEY_FACTS)
        ctx["key_facts"] = KeyFact.objects.all()
        return ctx


class OrganizationLeadershipView(TemplateView):
    template_name = "pages/organization_leadership.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["page"] = get_object_or_404(ContentPage, slug=ContentPage.Slugs.ORGANIZATION_LEADERSHIP)
        ctx["leaders"] = LeadershipMember.objects.all()
        return ctx


class OrganizationPerformanceView(TemplateView):
    template_name = "pages/organization_performance.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["page"] = get_object_or_404(ContentPage, slug=ContentPage.Slugs.ORGANIZATION_PERFORMANCE)
        ctx["items"] = PerformanceItem.objects.all()
        return ctx


class CareerView(TemplateView):
    template_name = "pages/career.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["page"] = get_object_or_404(ContentPage, slug=ContentPage.Slugs.CAREER)
        return ctx


class ContactView(TemplateView):
    template_name = "pages/contact.html"
