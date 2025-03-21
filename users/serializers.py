from rest_framework import serializers

from materials.models import Course, Lesson
from users.models import Payment, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']



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


class UserPaymentsSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True)

    class Meta:
        model = User
        fields = ["email", "payments"]

    def create(self, validated_data):
        payments_set = validated_data.pop("payments")

        user_object = User.objects.create(**validated_data)

        for payment in payments_set:
            Payment.objects.create(user=user_object, **payment)

        return user_object
