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

        paid_course_python, _ = Course.objects.get_or_create(
            name="Python", description="Python Description"
        )
        paid_course_sql, _ = Course.objects.get_or_create(
            name="Python", description="SQL Description"
        )

        paid_lesson_1, _ = Lesson.objects.get_or_create(
            name="Test Lesson Python 1", description="1 Test Description lesson python", course=paid_course_python
        )

        paid_lesson_2, _ = Lesson.objects.get_or_create(
            name="Test Lesson Python 2", description="2 Test Description lesson python", course=paid_course_python
        )
        paid_lesson_3, _ = Lesson.objects.get_or_create(
            name="Test Lesson SQL 1", description="1 Test Description lesson SQL", course=paid_course_sql
        )

        paid_lesson_4, _ = Lesson.objects.get_or_create(
            name="Test Lesson SQL 2", description="2 Test Description lesson SQL", course=paid_course_sql
        )
        paid_lesson_5, _ = Lesson.objects.get_or_create(
            name="Test Lesson Python 3", description="3 Test Description lesson python", course=paid_course_python
        )

        paid_lesson_6, _ = Lesson.objects.get_or_create(
            name="Test Lesson SQL 3", description="3 Test Description lesson SQL", course=paid_course_sql
        )
        user, _ = User.objects.get_or_create(email="user@user.com")

        another_user, _ = User.objects.get_or_create(email="anotheruser@anotheruser.com")

        payments = [
            {
                "user": user,
                "payment_date": "2020-01-01",
                "payment_summ": 100.0,
                "payment_mode": Payment.CARD,
                "paid_course": paid_course_python,
                "paid_lesson": paid_lesson_1,
            },
            {
                "user": user,
                "payment_date": "2010-02-02",
                "payment_summ": 200.0,
                "payment_mode": Payment.CARD,
                "paid_course": paid_course_python,
                "paid_lesson": paid_lesson_2,
            },
            {
                "user": user,
                "payment_date": "2016-06-08",
                "payment_summ": 867.0,
                "payment_mode": Payment.CASH,
                "paid_course": paid_course_sql,
                "paid_lesson": paid_lesson_3,
            },
            {
                "user": user,
                "payment_date": "2011-04-20",
                "payment_summ": 2765.89,
                "payment_mode": Payment.CASH,
                "paid_course": paid_course_sql,
                "paid_lesson": paid_lesson_4,
            },
            {
                "user": another_user,
                "payment_date": "2018-11-16",
                "payment_summ": 156.70,
                "payment_mode": Payment.CASH,
                "paid_course": paid_course_python,
                "paid_lesson": paid_lesson_5,
            },
            {
                "user": another_user,
                "payment_date": "2015-07-07",
                "payment_summ": 2380.89,
                "payment_mode": Payment.CARD,
                "paid_course": paid_course_sql,
                "paid_lesson": paid_lesson_6,
            },
        ]

        for payment_data in payments:
            Payment.objects.get_or_create(**payment_data)

        self.stdout.write(self.style.SUCCESS(f"Successfully added 6 test payments")),

