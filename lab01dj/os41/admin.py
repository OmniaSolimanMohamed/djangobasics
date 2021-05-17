from django.contrib import admin
from .models import Student, Track

class CustomStudent (admin.ModelAdmin):
    fieldsets = (
        ['studen Info',{'fields':['fname','lname']}],
        ['scholarship Info',{'fields':['age','student_track']}]
    )
    list_display = ('fname','lname','age','student_track','is_grad')
    list_filter = ['student_track']
    search_fields = ['fname']
class InlineStudent (admin.StackedInline):
    model = Student
    extra = 2

class CustomTrack (admin.ModelAdmin):
        inlines = [InlineStudent]
# Register your models here.
admin.site.register(Student, CustomStudent)
admin.site.register(Track, CustomTrack)
