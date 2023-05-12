from django.contrib import admin
from .models import coop


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(coop, QuestionAdmin)