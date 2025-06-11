from django.urls import path,include
from rest_framework import routers
from .views import CourseListViewSet,InstructorProfileViewSet,StudentRecordViewSet,SponsershipDetailViewSet


router = routers.DefaultRouter()
router.register(r'CourseList',CourseListViewSet)
router.register(r'InstructorProfiles',InstructorProfileViewSet)
router.register(r'StudentRecords',StudentRecordViewSet)
router.register(r'SponsershipDetail',SponsershipDetailViewSet)

urlpatterns = [
   
] + router.urls