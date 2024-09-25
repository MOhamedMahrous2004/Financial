from django.db import models

# Create your models here.

class Transaction(models.Model):
    transaction_date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.IntegerField()

    def __str__(self):
        return f"Transaction {self.id}:{self.description} - {self.amount}"
