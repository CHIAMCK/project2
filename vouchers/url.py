from django.urls import path
from .views.check_voucher import CheckVoucherView

app_name = 'voucher'

urlpatterns = [
    path('check', CheckVoucherView.as_view(), name='check_voucher')
]
