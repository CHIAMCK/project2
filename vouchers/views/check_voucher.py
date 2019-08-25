from django.shortcuts import render
from django.views.generic import FormView

from ..forms.voucher_check import CheckVoucherForm


class CheckVoucherView(FormView):
    form_class = CheckVoucherForm
    template_name = 'voucher_check.html'

    def form_valid(self, form):
        form.voucher.usage_limit = form.voucher.usage_limit - 1
        form.voucher.save(update_fields=['usage_limit'])
        return render(self.request, self.template_name,
                      context=self.get_context_data(
                      form=form, discount=form.voucher.discount))
