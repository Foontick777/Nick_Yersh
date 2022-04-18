from django.contrib import admin
from .models import Student, Book


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "age")


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'student', 'pages')
