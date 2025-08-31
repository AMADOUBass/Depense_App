"""
A simple model representing a financial transaction.
"""
import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Transaction(models.Model):
    """
    A model representing a financial transaction.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta options for the Transaction model.
        """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.description} - {self.amount}"
