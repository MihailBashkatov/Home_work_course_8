from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsOwner, ModeratorAccessPermission


class CourseViewSet(viewsets.ModelViewSet):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if ModeratorAccessPermission().has_permission(self.request, self):
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [~ModeratorAccessPermission, IsAuthenticated]
        elif self.action in ["update", "partial_update", "retrieve", "list"]:
            self.permission_classes = [
                IsAuthenticated,
                IsOwner | ModeratorAccessPermission,
            ]
        elif self.action == "destroy":
            self.permission_classes = [
                IsAuthenticated,
                ~ModeratorAccessPermission | IsOwner,
            ]
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [~ModeratorAccessPermission, IsOwner, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | ModeratorAccessPermission]

    def get_queryset(self):
        if ModeratorAccessPermission().has_permission(self.request, self):
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)


class LessonRetreiveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | ModeratorAccessPermission]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | ModeratorAccessPermission]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | ~ModeratorAccessPermission]
