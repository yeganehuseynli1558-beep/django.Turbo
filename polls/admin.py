
from django.contrib import admin
from django.contrib.auth.models import User
from .models import CarAd


# Parol tələb etmədən birbaşa daxil olan xüsusi Admin Panel
class PasswordlessAdminSite(admin.AdminSite):
  def has_permission(self, request):
    # Əgər bazada istifadəçi yoxdursa avtomatik 'admin' istifadəçisi yaradır
    user, _ = User.objects.get_or_create(
        username='admin', is_staff=True, is_superuser=True
    )
    request.user = user
    return True


# Yaratdığımız xüsusi admin paneli aktiv edirik
admin_site = PasswordlessAdminSite(name='passwordless_admin')
admin_site.register(CarAd)