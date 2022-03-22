from django.contrib import admin
from fees.models import Summary01, Summary02, Summary03, FeeCBC, SummaryFee, FeeADD, FeeCUP

# Register your models here.
admin.site.register(Summary01)
admin.site.register(Summary02)
admin.site.register(Summary03)
admin.site.register(FeeCBC)
admin.site.register(SummaryFee)
admin.site.register(FeeADD)
admin.site.register(FeeCUP)