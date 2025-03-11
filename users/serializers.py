from rest_framework import serializers

from materials.models import Course, Lesson
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
