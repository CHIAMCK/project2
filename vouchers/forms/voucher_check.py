from django import forms
from django.core.exceptions import ValidationError

from ..models import Voucher


class CheckVoucherForm(forms.Form):
    voucher_code = forms.CharField(label='Enter voucher code')

    def clean_voucher_code(self):
        voucher_code = self.cleaned_data['voucher_code']
        # if voucher code is not in the DB, it is invalid
        try:
            self.voucher = Voucher.objects.get(code__exact=voucher_code)
        except Voucher.DoesNotExist:
            raise ValidationError('Voucher code is invalid.')

        # if the voucher is used more than 3 times, voucher code is invalid
        if self.voucher.usage_limit <= 0:
            raise ValidationError('Voucher code is invalid.')
        return voucher_code
