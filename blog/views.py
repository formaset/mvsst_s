from django.views.generic import ListView, DetailView
from .models import Post


class BlogIndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 12

    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED).order_by("-published_at", "-created_at")


class BlogDetailView(DetailView):
    template_name = "blog/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED).order_by("-published_at", "-created_at")
