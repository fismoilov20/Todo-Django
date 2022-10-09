from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

# Register your models here.

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields = ('name',)
    list_filter = ('course',)
    list_display = ('id', 'std_id', 'name', 'age', 'course')
    list_display_links = ('name',)

@admin.register(Plan)
class PlanAdmin(ModelAdmin):
    search_fields = ('heading',)
    list_filter = ('done',)
    list_display = ('id', 'heading', 'date', 'done', 'student')
    list_display_links = ('heading',)
    autocomplete_fields = ('student',)

@admin.register(Todo)
class TodoAdmin(ModelAdmin):
    search_fields = ('heading', 'details')
    list_display = ('id', 'heading', 'done', 'student')
    
@admin.register(Account)
class AccountAdmin(ModelAdmin):
    search_fields = ('fullname',)
    list_display = ('id', 'fullname', 'user')