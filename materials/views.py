from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.paginators import MyPagination
from materials.serializers import (CourseSerializer, LessonSerializer,
                                   SubscriptionSerializer)
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
    pagination_class = MyPagination

    def get_queryset(self):
        if ModeratorAccessPermission().has_permission(self.request, self):
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)



    def get(self, request):
        queryset = Lesson.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = LessonSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


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


class SubscribeAPIView(APIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def post(self, request):
        user = request.user
        course_id = request.data.get("course")
        course = get_object_or_404(Course, id=course_id)

        subscription, created = Subscription.objects.get_or_create(
            user=user, course=course
        )

        if subscription.subscription == False:
            subscription.subscription = True
            subscription.save()
            message = "Subscription Added"

        elif subscription.subscription == True:
            subscription.subscription = False
            subscription.save()
            message = "Subscription Deleted"

        return Response({"message": {message}}, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        subscriptions = Subscription.objects.filter(user=user)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)
