from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateAPIView,
                             LessonDestroyAPIView, LessonListAPIView,
                             LessonRetreiveAPIView, LessonUpdateAPIView, SubscribeAPIView)

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetreiveAPIView.as_view(), name="lesson_detail"),
    path(
        "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
    path(
        "lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
    path("subscription/", SubscribeAPIView.as_view(), name="subscription")
] + router.urls

