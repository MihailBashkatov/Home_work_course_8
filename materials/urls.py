from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetreiveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='Lesson_create'),
    path('Lesson/', LessonListAPIView.as_view(), name='Lesson_list'),
    path('Lesson/<int:pk>/', LessonRetreiveAPIView.as_view(), name='Lesson_detail'),
    path('Lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='Lesson_update'),
    path('Lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='Lesson_delete'),

              ] + router.urls