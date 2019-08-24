from django import forms


class CheckVoucherForm(forms.Form):
    voucher_code = forms.CharField(label='Voucher code')
