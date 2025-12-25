from django.urls import path
from .views import (
    CareerView,
    ContactView,
    HomeView,
    OrganizationAboutView,
    OrganizationKeyFactsView,
    OrganizationLeadershipView,
    OrganizationPerformanceView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("organization/about/", OrganizationAboutView.as_view(), name="organization_about"),
    path("organization/key-facts/", OrganizationKeyFactsView.as_view(), name="organization_key_facts"),
    path("organization/leadership/", OrganizationLeadershipView.as_view(), name="organization_leadership"),
    path("organization/performance/", OrganizationPerformanceView.as_view(), name="organization_performance"),
    path("career/", CareerView.as_view(), name="career"),
    path("contact/", ContactView.as_view(), name="contact"),
]
