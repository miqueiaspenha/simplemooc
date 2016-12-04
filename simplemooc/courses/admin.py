from django.contrib import admin

# Register your models here.

from .models import (Course, Enrollment, Announcement, Comment, Lesson, Material)

class CommentInlineAdmin(admin.StackedInline):
	
	model = Comment

class MaterialInlineAdmin(admin.StackedInline):

	model = Material

class EnrollmentInlineAdmin(admin.StackedInline):
	model = Enrollment
	exclude = ['status']

class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ['title', 'content']
	search_fields = ['title']
	list_filter = ['created_at']

	inlines = [
		CommentInlineAdmin
	]

class LessonAdmin(admin.ModelAdmin):

	list_display = ['name', 'number', 'course', 'release_date']
	search_fields = ['name', 'description']
	list_filter = ['created_at']

	inlines = [
		MaterialInlineAdmin
	]

class CourseAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug', 'start_date', 'create_at']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

	inlines = [
		EnrollmentInlineAdmin
	]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Announcement, AnnouncementAdmin)