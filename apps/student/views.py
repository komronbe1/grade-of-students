from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveDestroyAPIView
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    