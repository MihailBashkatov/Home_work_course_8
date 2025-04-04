from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def send_update_course_info(users_list, course_name):
    """Task to send email about Course changing for subscribed users"""
    send_mail(
        subject=f"Updated info for course {course_name}",
        message=f"The course {course_name} has been updated. Please, check details",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=users_list,
    )
