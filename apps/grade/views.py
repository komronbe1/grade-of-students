from rest_framework import viewsets
from rest_framework.generics import RetrieveDestroyAPIView
from .models import Grade
from .serializers import GradeSerializer


class GradeViewSet(viewsets.ModelViewSet):

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class GradeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer