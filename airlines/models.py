from django.db import models
from model_utils import Choices
from django.utils import timezone

# Create your models here.




class Booking_History(models.Model):

    GENDER = Choices(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=50, null=True, blank=True)
    age = models.FloatField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=1, blank=True)
    booking_date = models.DateTimeField(default=timezone.now)
    from_place = models.CharField(max_length=30)
    to_place = models.CharField(max_length=30)
    seat_no =  models.IntegerField(null=True, blank=False)
    total_fare = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Booking History"
        verbose_name = ""


