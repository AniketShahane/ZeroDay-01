from django.shortcuts import render
from django.http import HttpResponse
from .models import Donor, RevenueAdded
from child.models import Child

# Create your views here.
def donors(request):
    donors = Donor.objects.order_by('-time')
    content = {
        'donors': donors
    }
    return render(request,'admin/tables.html',content)

def admin_panel(request):
    latestRev = RevenueAdded.objects.all().order_by('-time')[0].principal_amount
    donors = Donor.objects.all().count()
    children = Child.objects.all().count()
    topDonors = Donor.objects.all().order_by('-amount')[:4]

    return render(request, 'admin/dashboard.html', {'revenue': latestRev, 'donors':donors, 'children': children, 'topDonors': topDonors})

def children(request):
    children = Child.objects.all().order_by('-joined')
    content = {
        'children': children
    }
    return render(request, 'admin/icons.html', content)