from django.urls import path
from fees import views

urlpatterns = [
    path('', views.SummaryHome, name='summary-home'),
    path('import-fee-summary/', views.ImportSummaryFee, name='import-fee-summary'),
    path('fee-cbc/', views.FeeCBCHome, name='fee-cbc-home'),
    path('import-fee-cbc/', views.ImportFeeCBC, name='import-fee-cbc'),
    path('fee-qr/', views.FeeQRHome, name='fee-qr-home'),
    path('import-fee-qr/', views.ImportFeeQR, name='import-fee-qr'),
    path('fee-cup/', views.FeeCUPHome, name='fee-cup-home'),
    path('import-fee-cup/', views.ImportFeeCUP, name='import-fee-cup'),
    path('fee-napas/', views.FeeNapasHome, name='fee-napas-home'),
    path('import-fee-napas/', views.ImportFeeNapas, name='import-fee-napas'),
    path('sum-fee-home/', views.SumFeeHome, name='sum-fee-home'),
    path('summary-fee/', views.SumFee.as_view(), name='summary-fee'),
    path('summary-surcharge/', views.Summary01Home.as_view(), name='summary-surcharge'),
    path('summary-update/<int:pk>', views.UpdateSummary01.as_view(), name='summary-update'),
    path('updateSumFee/', views.UpdateSummaryFee, name='update-sum-fee'),
    path('handtable/', views.handson_table, name='handson_view'),
]

