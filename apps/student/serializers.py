from rest_framework import serializers
from .models import Student
from rest_framework.exceptions import ValidationError


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

    def validate_phone(self, value):
        if not value.startswith("+998"):
            raise ValidationError("Telefon +998 bilan boshlanishi kerak")
        return value

    def validate_email(self, value):
        if not value.endswith("@gmail.com"):
            raise ValidationError("Email oxiri @gmail.com bo'lishi kerak")
        return value