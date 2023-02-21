from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.



class Seller(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name
    
class Sale(models.Model):
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
    saller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)

SIZE_CLOTHES = (
    ('p','P'),
    ('m','M'),
    ('g','G')
)

class Clothe(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=1, choices=SIZE_CLOTHES)
    amount = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.name}({self.size})"

class ClotheItem(models.Model):
    price_unit = models.FloatField()
    amount_items = models.PositiveIntegerField()

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items", null=False)
    clothe = models.ForeignKey(Clothe, on_delete=models.CASCADE, null=False)
    def clean(self) -> None:
        if self.amount_items < self.clothe.amount:
            raise ValidationError("Amount Item more than Amount Clothes ")
        return super(ClotheItem, self).clean()

    def __str__(self) -> str:
        return f"{self.clothe}"

    
