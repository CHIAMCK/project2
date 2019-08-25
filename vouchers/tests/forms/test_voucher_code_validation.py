from django.core.exceptions import ValidationError
from django.test import TestCase
from grappa import should

from vouchers.forms.voucher_check import CheckVoucherForm
from vouchers.models import Voucher


class VoucherCodeValidationTest(TestCase):
    def setUp(self):
        Voucher.objects.create(code='e123', discount='10% off', usage_limit=3)
        Voucher.objects.create(code='voucher', discount='10% off', 
                               usage_limit=0)

    def test_clean_voucher_code_pass(self):
        # set up
        f = CheckVoucherForm()
        f.cleaned_data = {'voucher_code': 'e123'}

        # execution
        outcome = f.clean_voucher_code()

        # assertion
        outcome | should.equal('e123')

    def test_clean_voucher_code_invalid_voucher_code(self):
        # set up
        f = CheckVoucherForm()
        f.cleaned_data = {'voucher_code': 'abc'}

        # execution
        with self.assertRaises(ValidationError) as cm:
            f.clean_voucher_code()

        # assertion
        cm.exception | should.have.property('message').that.equal('Voucher code is invalid.')

    def test_clean_voucher_code_used_more_than_3_times(self):
        # set up
        f = CheckVoucherForm()
        f.cleaned_data = {'voucher_code': 'voucher'}

        # execution
        with self.assertRaises(ValidationError) as cm:
            f.clean_voucher_code()

        # assertion
        cm.exception | should.have.property('message').that.equal('Voucher code is invalid.')
