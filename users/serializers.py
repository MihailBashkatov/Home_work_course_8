from rest_framework import serializers

from materials.models import Course, Lesson
from users.models import Payment, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            "user",
            "payment_date",
            "payment_summ",
            "payment_mode",
            "paid_course",
            "paid_lesson",
        ]
