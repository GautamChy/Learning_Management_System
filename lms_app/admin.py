from django.contrib import admin
from .models import CourseList,InstructorProfile,StudentRecord,SponsershipDetail,Assessment
# Register your models here.
class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = ('id','InstructorName','bio')
admin.site.register(InstructorProfile,InstructorProfileAdmin)

class CourseListAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','instructor','difficulty_level')
    search_fields = ('name','instructor__InstructorName','difficulty_level')
admin.site.register(CourseList,CourseListAdmin)

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
admin.site.register(Assessment,AssessmentAdmin)
class StudentsRecordsAdmin(admin.ModelAdmin):
    list_display = ('id','name','course','complete_assessment')
admin.site.register(StudentRecord,StudentsRecordsAdmin)

class SponsershipDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','students','status')
admin.site.register(SponsershipDetail,SponsershipDetailsAdmin)