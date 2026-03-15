from rest_framework import viewsets
from rest_framework.generics import RetrieveDestroyAPIView
from .models import Teacher
from .serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer