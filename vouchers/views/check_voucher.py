from django.views.generic import FormView
from ..forms.voucher_check import CheckVoucherForm


class CheckVoucherView(FormView):
    form_class = CheckVoucherForm
    template_name = 'voucher_check.html'