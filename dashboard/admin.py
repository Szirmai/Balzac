from django.contrib import admin
from . import models
from django.urls import reverse
from django.utils.html import format_html
from django.shortcuts import redirect
from django.urls import path


admin.site.register(models.Task)

class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('groups/', self.admin_view(self.manage_groups), name='groups'),
        ]
        return my_urls + urls

    def manage_groups(self, request):
        return redirect(reverse('groups'))

admin_site = CustomAdminSite(name='custom-admin')

