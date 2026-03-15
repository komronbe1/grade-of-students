from rest_framework import viewsets
from rest_framework.generics import RetrieveDestroyAPIView
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer