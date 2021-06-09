from loan_management.constants import LOAN_STATUS_MAPPING
from django.contrib.auth import get_user_model
from django.db import models


class ProductMapping(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(
        null=False, blank=False, default=None, max_length=20
    )
    prodcut_interest = models.IntegerField(null=False, blank=False, default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.product_name


class Loan(models.Model):

    status_choices = [
        ("Approved", LOAN_STATUS_MAPPING["APPROVED"]),
        ("Rejected", LOAN_STATUS_MAPPING["REJECTED"]),
        ("New", LOAN_STATUS_MAPPING["NEW"]),
    ]

    User = get_user_model()

    loan_id = models.BigAutoField(primary_key=True)
    interest_rate = models.IntegerField(default=10)
    amount = models.BigIntegerField(null=False, blank=False, default=1000)
    emi = models.IntegerField(null=False, default=0, blank=False)
    tenure = models.IntegerField(null=False, default=12, blank=False)
    status = models.IntegerField(choices=status_choices, default=3)
    extra_details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(to=ProductMapping, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user")
    agent = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, null=True, related_name="agent"
    )

    def save(self, *args, **kwargs):
        r = self.interest_rate / (100 * 12)
        self.emi = (
            self.amount * r * ((1 + r) ** self.tenure) / ((1 + r) ** self.tenure - 1)
        )
        super(Loan, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username
