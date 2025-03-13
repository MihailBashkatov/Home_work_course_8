from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = "Add test payments to the database"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        User.objects.all().delete()
        Course.objects.all().delete()
        Lesson.objects.all().delete()

        paid_course, _ = Course.objects.get_or_create(
            name="Test Course 1", description="Test Description"
        )
        paid_lesson, _ = Lesson.objects.get_or_create(
            name="Test Lesson 1", description="Test Description", course=paid_course
        )
        user, _ = User.objects.get_or_create(email="user@user.com")

        payments = [
            {
                "user": user,
                "payment_date": "2020-01-01",
                "payment_summ": 100.0,
                "payment_mode": Payment.CASH,
                "paid_course": paid_course,
                "paid_lesson": paid_lesson,
            },
            {
                "user": user,
                "payment_date": "2010-02-02",
                "payment_summ": 200.0,
                "payment_mode": Payment.CARD,
                "paid_course": paid_course,
                "paid_lesson": paid_lesson,
            },
        ]

        for payment_data in payments:
            payment, created = Payment.objects.get_or_create(**payment_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added payment")),
            else:
                self.stdout.write(self.style.WARNING(f"Payment already exists"))
