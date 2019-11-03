from django.db import models
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
MAX_JOB_SWIPES_ALLOWED = 50



class Tag(models.Model):
	tag = models.CharField(max_length=64, unique=True)

class Job(models.Model):
    employer_id = models.PositiveIntegerField()
    right_swipes = ArrayField(models.TextField(), null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tags')
    def __str__(self):
        return '%s'%(self.details.job_name)

class Details(models.Model):
	job = models.OneToOneField(Job, related_name='details', on_delete=models.CASCADE)
	job_name = models.CharField(max_length=100)
	date = models.DateField(null=False)
	time_from = models.TimeField()
	time_to = models.TimeField()
	duration = models.DurationField()
	pay_per_hour = models.DecimalField(decimal_places=2, max_digits=12)
	address = models.TextField()
	description = models.TextField()
	required_experience = models.TextField()

class Status(models.Model):
    job = models.OneToOneField(Job, related_name='status', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    pay = models.BooleanField(default=False)
    worker_time_in = models.TimeField(null=True, blank=True)
    worker_time_out = models.TimeField(null=True, blank=True)
    amount_paid = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
