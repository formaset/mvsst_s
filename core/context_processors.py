from .models import SiteSettings


def site_settings(request):
    obj = SiteSettings.objects.first()
    return {"site": obj}
