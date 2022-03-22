from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import ListView, UpdateView
import django_excel as excel
from django import forms
from fees.models import Summary01, Summary02, Summary03, SummaryFee, FeeCBC, FeeQR, FeeADD, FeeCUP, SummaryATM
from django.db.models import Sum, F
from django.urls import reverse_lazy
from django.db import transaction
from fees.forms import Summary01Form
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalFormView,
    BSModalReadView,
    BSModalUpdateView,
)

# Create your views here.

class SumFee(ListView):
    model = SummaryFee
    context_object_name = 'fees'
    template_name = 'fee_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["branch_sum"] = SummaryFee.objects.count()
        context["atm_sum"] = SummaryFee.objects.aggregate(Sum('fee_atm'))['fee_atm__sum']
        context["surcharge_sum"] = SummaryFee.objects.aggregate(Sum('fee_surcharg'))['fee_surcharg__sum']
        context["napas_sum"] = SummaryFee.objects.aggregate(Sum('fee_napas'))['fee_napas__sum']
        context["fee_sum"] = SummaryFee.objects.aggregate(Sum('fee_sum'))['fee_sum__sum']
        context["fee_atm"] = SummaryATM.objects.all()
        context["sum_atm_fee"] = SummaryATM.objects.aggregate(Sum('atm_sum'))['atm_sum__sum']
        context["sum_surcharge_fee"] = SummaryATM.objects.aggregate(Sum('surcharge_sum'))['surcharge_sum__sum']
        context["sum_napas_fee"] = SummaryATM.objects.aggregate(Sum('napas_sum'))['napas_sum__sum']
        context["sum_fee"] = SummaryATM.objects.aggregate(Sum('fee_sum'))['fee_sum__sum']
        context["from_date"] = Summary01.objects.all()[1]
        context["to_date"] = Summary01.objects.all()[2]

        return context
    

class Summary01Home(ListView):
    context_object_name = 'sum01s'
    template_name = 'fee_surcharge.html'

    def get_queryset(self):
        queryset = ""
        if self.request.GET.get("FeeReturn"):
            selection = self.request.GET.get("FeeReturn")
            queryset = Summary01.objects.filter(TERMINALID=selection)
        return queryset

class UpdateSummary01(BSModalUpdateView):
    model = Summary01
    template_name = 'summary_update.html'
    form_class = Summary01Form
    success_message = 'Thành công: Sự kiện đã được cập nhật!'
    success_url = reverse_lazy('summary-surcharge')

def SummaryHome(request):
    return render(request, 'summary_home.html')

def FeeCBCHome(request):
    return render(request, 'fee_cbc.html')

def FeeQRHome(request):
    return render(request, 'fee_qr.html')

def FeeCUPHome(request):
    return render(request, 'fee_cup.html')

def FeeNapasHome(request):
    return render(request, 'fee_napas.html')

def SumFeeHome(request):
    return render(request, 'sum_fee.html')
    
def UpdateSummaryFee(request):
    SummaryATM.objects.all().delete()
    tb1 = Summary01.objects.all()
    tb2 = Summary02.objects.all()
    tb3 = Summary03.objects.all()
    tb4 = SummaryATM.objects.all()
    tb = SummaryFee.objects.all()
    cbc = FeeCBC.objects.all()
    qr = FeeQR.objects.all()
    napas = FeeADD.objects.all()
    cup = FeeCUP.objects.all()

    Summary01.objects.update(FUNDCOUNT = 0, FUNDAMOUNT = 0, FUNDFEE = 0)
    Summary02.objects.update(CBCFEE = 0)
    Summary02.objects.update(CBQFEE = 0)
    listTrangBang = ['11880791', '13650791', '08820791', '08810791']
    Summary01.objects.filter(TERMINALID__in = listTrangBang).update(BRANCH = '4107')
    Summary02.objects.filter(TERMINALID__in = listTrangBang).update(BRANCH = '4107')
    Summary03.objects.filter(TERMINALID__in = listTrangBang).update(BRANCH = '4107')
    Summary01.objects.filter(TERMINALID = '03760924').update(BRANCH = '0647')
    Summary02.objects.filter(TERMINALID = '03760924').update(BRANCH = '0647')
    Summary03.objects.filter(TERMINALID = '03760924').update(BRANCH = '0647')
    SummaryFee.objects.update(fee_atm = 0, fee_surcharg = 0, fee_napas = 0, fee_sum = 0)
    
    for t2 in tb2:
        if t2.TERMINALID is not None:
            for cb in cbc:
                if t2.TERMINALID == cb.terminal_id:
                    t2.CBCFEE = cb.fee_cbc * 5500
            for q in qr:
                if t2.TERMINALID == q.terminal_id:
                    t2.CBQFEE = q.fee_qr
    Summary02.objects.bulk_update(tb2, ['CBCFEE'])
    Summary02.objects.bulk_update(tb2, ['CBQFEE'])

    for t1 in tb1:
        if  t1.TERMINALID is not None:
            for na in napas:
                if t1.PRODUCTNAME == na.name_produc:
                    t1.FUNDCOUNT = na.fee_01
                    t1.FUNDAMOUNT = na.fee_02
            if t1.PRODUCTNAME == 'UPI':
                for cu in cup:
                    if t1.TERMINALID == cu.terminal_id:
                        t1.FUNDFEE = cu.fee_cup
            t1.fee_napas = round(((t1.ATMCOUNT * t1.FUNDCOUNT) + (t1.BALCOUNT * t1.FUNDAMOUNT) + t1.FUNDFEE)/1.1)
    Summary01.objects.bulk_update(tb1, ['fee_napas'])

    #Tạo danh sách ATM theo Terminal ID
    list_atm = Summary01.objects.filter(TERMINALID__isnull = False).values_list('BRANCH', 'ATMNAME', 'TERMINALID').distinct()
    SummaryATM.objects.bulk_create([
        SummaryATM(**{
            'branch': m[0],
            'atm_name': m[1],
            'terminal_id': m[2],
        }) for m in list_atm
    ])

    for t in tb:
        result01 = 0
        result02 = 0
        result03 = 0
        result04 = 0
        result01 = Summary02.objects.filter(BRANCH = t.code_unit).aggregate(atm=Sum('ATMFEE'), bal=Sum('BALFEE'), min=Sum('MINIFEE'), fund=Sum('FUNDFEE'), nac=Sum('NACFEE'), cbc=Sum('CBCFEE'), qr=Sum('CBQFEE'))
        result02 = Summary03.objects.filter(BRANCH = t.code_unit).aggregate(atm=Sum('ATMFEE'), bal=Sum('BALFEE'), min=Sum('MINIFEE'), fund=Sum('FUNDFEE'), nac=Sum('NACFEE'))
        result03 = Summary01.objects.filter(BRANCH = t.code_unit).aggregate(sur=Sum('SURCHARGEFEE'), re=Sum('fee_return'))
        result04 = Summary01.objects.filter(BRANCH = t.code_unit).aggregate(fee_napas=Sum('fee_napas'))
        if result01['cbc'] != None:
            if  result01['atm'] is None:
                q1 = 0
            else:
                q1 = round((result01['atm'] + result01['bal'] + result01['min'] + result01['fund'] + result01['nac'] + result01['cbc'] + result01['qr'])/1.1)
            if result02['atm'] is None or result02['bal'] is None or result02['fund'] is None or result02['min'] is None or result02['nac'] is None:
                q2 = 0
            else:    
                q2 = round((result02['atm'] + result02['bal'] + result02['min'] + result02['fund'] + result02['nac'])/1.1)
            q3 = round((result03['sur'] - result03['re'])/1.1)
            q4 = result04['fee_napas']
            t.fee_atm = q1 + q2
            t.fee_surcharg = q3
            t.fee_napas = q4
            t.fee_sum = q1 + q2 + q3 + q4
    SummaryFee.objects.bulk_update(tb, ['fee_atm'])
    SummaryFee.objects.bulk_update(tb, ['fee_surcharg'])
    SummaryFee.objects.bulk_update(tb, ['fee_napas'])
    SummaryFee.objects.bulk_update(tb, ['fee_sum'])

    for t4 in tb4:
        sum01 = 0
        sum02 = 0
        for t2 in tb2:
            if t4.terminal_id == t2.TERMINALID:
                sum01 = t2.ATMFEE + t2.BALFEE + t2.MINIFEE + t2.FUNDFEE + t2.NACFEE + t2.CBCFEE
        for t3 in tb3:
            if t4.terminal_id == t3.TERMINALID:
                sum02 = t3.ATMFEE + t3.BALFEE + t3.MINIFEE + t3.FUNDFEE + t3.NACFEE
        t4.atm_sum = round((sum01 + sum02)/1.1)
        result03 = Summary01.objects.filter(TERMINALID__isnull = False).filter(TERMINALID = t4.terminal_id).aggregate(sur=Sum('SURCHARGEFEE'), re=Sum('fee_return'))
        result04 = Summary01.objects.filter(TERMINALID__isnull = False).filter(TERMINALID = t4.terminal_id).aggregate(napas = Sum('fee_napas'))
        t4.surcharge_sum = round((result03['sur'] - result03['re'])/1.1)
        t4.napas_sum = result04['napas']
        t4.fee_sum = t4.atm_sum + t4.surcharge_sum + t4.napas_sum

    SummaryATM.objects.bulk_update(tb4, ['atm_sum'])
    SummaryATM.objects.bulk_update(tb4, ['surcharge_sum'])
    SummaryATM.objects.bulk_update(tb4, ['napas_sum'])
    SummaryATM.objects.bulk_update(tb4, ['fee_sum'])

    return redirect('summary-fee')

def ImportFeeCBC(request):
    if request.method == "POST":
        FeeCBC.objects.all().delete()
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES["file"].save_to_database(
                model=FeeCBC,
            )
            return redirect('fee-qr-home')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request, "upload_form.html", {"form": form, "header": "Import file Phí CBC: fee_cbc.xlsx",})

def ImportFeeQR(request):
    if request.method == "POST":
        FeeQR.objects.all().delete()
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES["file"].save_to_database(
                model=FeeQR,
            )
            return redirect('fee-cup-home')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request, "upload_form.html", {"form": form, "header": "Import file Phí QR: fee_qr.xlsx",})

def ImportFeeNapas(request):
    if request.method == "POST":
        FeeADD.objects.all().delete()
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES["file"].save_to_database(
                model=FeeADD,
            )
            return redirect('summary-surcharge')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request, "upload_form.html", {"form": form, "header": "Import file Phí Napas: fee_napas.xlsx",})

def ImportFeeCUP(request):
    if request.method == "POST":
        FeeCUP.objects.all().delete()
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES["file"].save_to_database(
                model=FeeCUP,
            )
            return redirect('fee-napas-home')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request, "upload_form.html", {"form": form, "header": "Import file Phí CUP: fee_cup.xlsx",})

def ImportSummaryFee(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            Summary01.objects.all().delete()
            Summary02.objects.all().delete()
            Summary03.objects.all().delete()

            request.FILES["file"].save_book_to_database(
                models=[Summary01, Summary02, Summary03],
                bulk_save=True,
                mapdicts=[
                    {"BRANCH":"BRANCH", "ATMNAME":"ATMNAME", "PRODUCTNAME":"PRODUCTNAME", "TERMINALID":"TERMINALID", "ATMCOUNT":"ATMCOUNT", "BALCOUNT":"BALCOUNT", "SURCHARGEFEE":"SURCHARGEFEE"},
                    {"BRANCH":"BRANCH", "ATMNAME":"ATMNAME", "TERMINALID":"TERMINALID", "ATMFEE":"ATMFEE", "BALFEE":"BALFEE", "MINIFEE":"MINIFEE", "FUNDFEE":"FUNDFEE", "NACFEE":"NACFEE", "CBCFEE":"CBCFEE", "CBQFEE":"CBQFEE"},
                    {"BRANCH":"BRANCH", "ATMNAME":"ATMNAME", "TERMINALID":"TERMINALID", "ATMFEE":"ATMFEE", "BALFEE":"BALFEE", "MINIFEE":"MINIFEE", "FUNDFEE":"FUNDFEE", "NACFEE":"NACFEE"},
                ]
            )
            return redirect('fee-cbc-home')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        "upload_form.html",
        {
            "form": form,
            "header": "Vui lòng import file Phí Tổng: SummaryMonthly_...",
        },
    )

def handson_table(request):
    return excel.make_response_from_tables(
        [Summary01], "handsontable.html"
    )

class UploadFileForm(forms.Form):
    file = forms.FileField()