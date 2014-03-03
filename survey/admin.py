from django.contrib import admin
from survey.models import Survey, Question, Answer, CompletedSurvey


class QuestionInlineAdmin(admin.TabularInline):
    model = Question
    extra = 5

class AnswerInlineAdmin(admin.TabularInline):
    model = Answer
    extra = 5

class SurveyAdmin(admin.ModelAdmin):
    list_display = ("id", "posted",)
    search_fields = ("question",)
    inlines = [QuestionInlineAdmin]

class CompletedSurveyAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineAdmin]

admin.site.register(Survey, SurveyAdmin)
admin.site.register(CompletedSurvey, CompletedSurveyAdmin)
admin.site.register(Question)
admin.site.register(Answer)
