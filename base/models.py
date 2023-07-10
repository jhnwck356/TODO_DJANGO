from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    INCOMPLETE = 'incomplete'
    IN_PROGRESS = 'in progress'
    COMPLETED = 'Completed'

    STATUS_CHOICE = [
    (INCOMPLETE ,'incomplete'),
    (IN_PROGRESS , 'in progress'),
    (COMPLETED, 'Completed')
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default=INCOMPLETE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    targeted_completion_date = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'user'

    def remaining_days_until_completion(self):
        if self.targeted_completion_date:
            today = timezone.now().date()
            remaining_days = (self.targeted_completion_date - today).days
            return max(0, remaining_days)
        return None        