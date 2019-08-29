from django.shortcuts import render
from django.views.generic import FormView

from ..forms.voucher_check import CheckVoucherForm


class CheckVoucherView(FormView):
    ''' A view to check the validity of voucher'''
    
    form_class = CheckVoucherForm
    template_name = 'voucher_check.html'

    def form_valid(self, form):
        # record the usage of voucher
        form.voucher.usage_limit = form.voucher.usage_limit - 1
        form.voucher.save(update_fields=['usage_limit'])
        # render the form with voucher code and discount value
        return render(self.request, self.template_name,
                      context=self.get_context_data(
                      form=form, discount=form.voucher.discount))
