from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "course", "owner"]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    #
    @staticmethod
    def get_lessons_count(course):
        """Getting amount of lessons per course"""
        return course.lessons.all().count()

    class Meta:
        model = Course
        fields = ["id", "name", "description", "lessons_count", "lessons", "owner"]
