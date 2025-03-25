from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            LinkValidator(field=['url_link'])]


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
        fields = "__all__"

