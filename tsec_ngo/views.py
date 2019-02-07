from django.shortcuts import render, redirect
from donor.models import Donor, RevenueAdded
from django.core.mail import EmailMessage
import random
import json
from child.models import Child
from feedback.models import Feedback



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

def addChild(request):
    if request.method == 'POST':
        name = request.POST['name']
        village = request.POST['village']
        ambitions = request.POST['ambitions']
        year = random.choices((2015, 2016,2017,2018))
        grades = random.randint(50,100)
        grade = json.dumps({year[0]: grades})
        mentor = random.choices(('Kavita Patil', 'Diya Patil', 'Ramesh Sahu'))[0]
        newChild = Child(name=name, village=village, ambition=ambitions, grades=grade, mentor=mentor)
        newChild.save()
        return redirect('children')

def giveFeedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        feed = Feedback(name=name, email=email, phone=phone, message=message)
        feed.save()
        return redirect('home')
        
