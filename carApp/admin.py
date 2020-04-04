from django import forms
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from .models import Car, Comment, Profile


# Register your models here.


class CarAdminForm(forms.ModelForm):
    name_ru = forms.CharField(label="Марка")
    name_en = forms.CharField(label="Марка")


admin.site.register(Car)
admin.site.register(Comment)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_user = ("user", "first_name")
