from django.contrib import admin

# Register your models here.

from .models import Course

class CourseAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug', 'start_date', 'create_at']
	search_fields = ['name', 'slug']

admin.site.register(Course, CourseAdmin)