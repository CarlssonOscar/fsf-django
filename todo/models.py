from django.db import models

# Create your models here.
class Item(models.Model):
    # CharField means it will have caracters or text.
    name = models.CharField(max_length=50, null=False, blank=False)
    # Boolean = true or false
    done = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.name