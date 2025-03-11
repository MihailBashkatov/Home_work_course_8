from django.db import models

class Course(models.Model):
    """ Registering model Course """
    name = models.CharField(
        max_length=300,
        verbose_name="Name",
    )

    description = models.TextField(
        verbose_name="Description"
    )

    preview = models.ImageField(
        upload_to="materials/course/preview/%Y/%m/%d/",
        default=None,
        null=True,
        blank=True,
        verbose_name="Saved course preview",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["name",]


class Lesson(models.Model):
    """ Registering model Lesson """
    name = models.CharField(
        max_length=300,
        verbose_name="Name",
    )

    description = models.TextField(
        verbose_name="Description"
    )

    preview = models.ImageField(
        upload_to="materials/lessons/preview/%Y/%m/%d/",
        default=None,
        null=True,
        blank=True,
        verbose_name="Saved course preview",
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False, related_name="lessons")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ["name",]
