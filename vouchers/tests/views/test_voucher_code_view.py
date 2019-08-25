from django.test import RequestFactory, TestCase
from grappa import should

from vouchers.forms.voucher_check import CheckVoucherForm
from vouchers.models import Voucher
from vouchers.views.check_voucher import CheckVoucherView


class CheckVoucherViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.v1 = Voucher.objects.create(code='e123', discount='10% off',
                                         usage_limit=3)
        Voucher.objects.create(code='voucher', discount='10% off',
                               usage_limit=0)

    def test_check_voucher_view(self):
        # set up
        kwargs = {}
        f = CheckVoucherForm()
        f.voucher = self.v1
        request = self.factory.get('/test')
        view = CheckVoucherView(kwargs=kwargs)
        view.request = request

        # execution
        response = view.form_valid(f)

        # assertion
        voucher_after_check = Voucher.objects.get(code='e123')
        voucher_after_check.usage_limit | should.equal(2)
        response.status_code | should.equal(200)
