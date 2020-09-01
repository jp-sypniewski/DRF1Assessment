from django.db import models


# Create your models here.
class JobOffer(models.Model):
    company_name = models.CharField(max_length=120)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=120)
    job_description = models.CharField(max_length=120)
    salary = models.PositiveIntegerField()
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"
