from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CourseList,InstructorProfile,StudentRecord,SponsershipDetail,Assessment
from .serializers import CourseSerializer,InstructorProfileSerializer,StudentRecordSerializer,SponsershipDetailSerializer,AssessmentSerializer
from rest_framework import filters
from django_filters import rest_framework as filter
from rest_framework.pagination import PageNumberPagination
# Create your views here.


# Modify Pagination
class Pages(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
class CourseListViewSet(ModelViewSet):
    queryset = CourseList.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','instructor__InstructorName','difficulty_level','assessment']
    pagination_class = Pages
    
    # Modify Pagination
class Pages(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
class InstructorProfileViewSet(ModelViewSet):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer
    pagination_class = Pages
    
    # Modify Pagination
class Pages(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
class StudentRecordViewSet(ModelViewSet):
    queryset = StudentRecord.objects.all()
    serializer_class = StudentRecordSerializer
    pagination_class = Pages
    
    # Modify Pagination
class Pages(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
class SponsershipDetailViewSet(ModelViewSet):
    queryset = SponsershipDetail.objects.all()
    serializer_class = SponsershipDetailSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filterset_fields = ['status',]
    pagination_class = Pages
    
    # Modify Pagination
class Pages(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
class AssessmentViewSet(ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    pagination_class = Pages
    
    