from django.views.generic import TemplateView
from blog.models import Post


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["latest_posts"] = Post.objects.filter(status=Post.Status.PUBLISHED).order_by("-published_at", "-created_at")[:8]
        return ctx


class AboutView(TemplateView):
    template_name = "pages/about.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"
