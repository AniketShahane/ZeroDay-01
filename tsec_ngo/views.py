from django.shortcuts import render, redirect
from donor.models import Donor, RevenueAdded
from django.core.mail import EmailMessage


def home(request):
    return render(request, 'index.html')

def donate(request):
    if request.method == 'POST':
        name = request.POST['name']
        emailid = request.POST['email']
        area = request.POST['area']
        amount = request.POST['amount']
        new_donor = Donor(name=name, email=emailid, area=area, amount=int(amount))
        new_donor.save()
        latestAddRev = RevenueAdded.objects.order_by('-time')[0].principal_amount if RevenueAdded.objects.all() else 0
        addRev = RevenueAdded()
        addRev.principal_amount = latestAddRev + new_donor.amount 
        addRev.donor_id = new_donor
        addRev.save()
        email=EmailMessage('Thank you for donating','We have recieved your donation, thank you for contributing towards our family. Every helping hand helps our family get stronger. Here is a receipt for your Donation. Here are your transaction details :: Donated amount :'+amount+'From : '+name+' .To : HackZeroDay@1234'+' .Location : '+area,to=[emailid])
        email.send()
        return redirect('home')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username.strip() == 'Aniket' and password == 'aniket@123':
            return redirect('admin_panel')
        else: 
            return redirect('login')
    return render(request, 'login.html')
