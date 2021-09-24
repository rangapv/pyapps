from django.contrib import admin

# Register your models here.

from polls.models import Question,Choice
admin.site.site_header=”surveyEarth Admin”
admin.site.site_title=”surveyEarth Admin Page”
admin.site.index_title=”Welcome to the surveyEarth Admin Page”
class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{‘fields’:[‘question_text’]}),
    (‘Date Information’,{‘fields’:[‘pub_date’],’classes’:[‘collapse’]}),]
    inlines=[ChoiceInLine]
admin.site.register(Question,QuestionAdmin)
