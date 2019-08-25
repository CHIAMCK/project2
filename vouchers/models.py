from django.db import models


class Voucher(models.Model):

    code = models.CharField(max_length=191)

    discount = models.CharField(max_length=191)

    usage_limit = models.PositiveIntegerField(default=3)
