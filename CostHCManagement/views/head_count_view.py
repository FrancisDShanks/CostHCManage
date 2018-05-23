from django.shortcuts import render
from django.shortcuts import get_list_or_404
from CostHCManagement.models import *
# Create your views here.


def get_quarter(month):
    if month < 1 or month > 12:
        return "FXXC"
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    else:
        return 4

def index(request):
    if request.method == 'GET':
        records = get_list_or_404(HeadCount)
        projects = get_list_or_404(CHCMProject)
        roles = get_list_or_404(CHCMRole)

        return render(request, 'index.html', {'projects': projects, 'hc': records})
    if request.method == 'POST':
        reg = request.POST.get('hc_reg')
        ot = request.POST.get('hc_ot')
        date = request.POST.get('hc_date')
        role = request.POST.get('hc_role')
        project = request.POST.get('hc_project')
        year = int(date[:4])
        month = int(date[5:7])
        financial_year = year + 1
        quarter = get_quarter(month)

        HeadCount.objects.create(
            date=date,
            headcountreg=reg,
            headcountot=ot,
            role_id=int(role),
            project_id=int(project),
            year=year,
            month=month,
            financial_year=financial_year,
            quarter=quarter
        )
        records = get_list_or_404(HeadCount)
        projects = get_list_or_404(CHCMProject)
        roles = get_list_or_404(CHCMRole)
        return render(request, 'index.html', {'projects': projects, 'hc': records})


def test(request):
    a = 'test'
    return render(request, 'test.html', {'a': a})
