from django.db import models

class Current(models.Model):
    semester = models.ForeignKey(
        'Semester',
        on_delete = models.CASCADE
    )
    progress = models.IntegerField(default=0)    # 0: just created, 1: auditioning, 2: finished

class Semester(models.Model):
    title = models.CharField(max_length=32, unique=True)
    audition_date = models.DateField()

class SemesterSchedule(models.Model):
    semester = models.ForeignKey(
        'Semester',
        on_delete = models.CASCADE
    )
    day = models.CharField(max_length=9)
    time = models.CharField(max_length=7)   # format: [hr]_[min][AM/PM]
    value = models.CharField(max_length=32, blank=True)
    type = models.CharField(max_length=32, blank=True)

    class Meta:
        unique_together = ("semester", "time", "day")

class Dancer(models.Model):
    first_name = models.CharField(max_length=16)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=16)
    email = models.EmailField()

class Auditionee(models.Model):
    semester = models.ForeignKey(
        'Semester',
        on_delete = models.CASCADE
    )
    dancer = models.ForeignKey(
        'Dancer',
        on_delete = models.CASCADE
    )
    dancer_number = models.IntegerField()
    choreographer = models.BooleanField(default=False)
    notes = models.TextField()

    class Meta:
        unique_together = ("semester", "dancer")

class DancerSchedule(models.Model):
    audition = models.ForeignKey(
        'Auditionee',
        on_delete = models.CASCADE
    )
    day = models.CharField(max_length=9)
    time = models.CharField(max_length=7)   # format: [hr]_[min][AM/PM]
    value = models.BooleanField(default=False)

    class Meta:
        unique_together = ("audition", "time", "day")
