from rest_framework import serializers

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    #
    @staticmethod
    def get_lessons(course):
        """ Getting amount of lessons per course"""
        return course.lessons.all().count()

    class Meta:
        model = Course
        fields = ["id", "name", "description", "lessons"]


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "course"]
