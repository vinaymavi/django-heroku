from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class AdminQuestion(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ("Date Information", {'fields': ['pub_date']})
    ]
    inlines=[ChoiceInline]
    list_display=['question_text','pub_date','was_published_recently']

admin.site.register(Question, AdminQuestion)
