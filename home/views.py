from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Customers, Transactions
from datetime import date, datetime
from django.db import connection

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def customers(request):
    customers = Customers.objects.all()
    return render(request, 'home/customers.html', {'customers' : customers})

def user(request):
    info = {}
    if (request.method=='POST'):
        unique_id = request.POST['hidden_unique_id']
        user_info = Customers.objects.raw("SELECT * FROM home_customers where id='"+unique_id+"'")
        info["id"] = user_info[0].id
        info["name"] = user_info[0].name
        info["email"] = user_info[0].email
        info["contact_no"] = user_info[0].contact_no
        info["dob"] = user_info[0].dob
        info["gender"] = user_info[0].gender
        info["current_balance"] = user_info[0].current_balance
    return render(request, "home/details.html", context=info)

def send_money(request):
    info = ''
    unique_id = ''
    customers = Customers.objects.all()
    if (request.method=='POST'):
        unique_id = request.POST['hidden_unique_id']
        user_info = Customers.objects.raw("SELECT * FROM home_customers where id='"+unique_id+"'")
        info = user_info[0].current_balance

    return render(request, "home/send_money.html", {'customers': customers, 'info': info, 'sender_id': int(unique_id)})

def transaction_done(request):
    if (request.method=='POST'):
        amount = request.POST['amount']
        reciever_id = request.POST['reciever']
        sender_id = request.POST['sender_id']
        reciever_query = Customers.objects.raw("SELECT * FROM home_customers where id='"+reciever_id+"'")
        sender_query = Customers.objects.raw("SELECT * FROM home_customers where id='"+sender_id+"'")
        reciever_name = reciever_query[0].name
        sender_name = sender_query[0].name
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(today, current_time)
        with connection.cursor() as cursor:
            cursor.execute("update home_customers set current_balance = current_balance - {} where id={}".format( int(amount), sender_id))
            cursor.execute("update home_customers set current_balance = current_balance + {} where id={}".format(int(amount), reciever_id))
            cursor.execute("insert into home_transactions (reciever, sender, date,time, amount) values ('{}', '{}', '{}','{}',{});".format(reciever_name, sender_name, today, current_time, amount))

    return redirect('/transaction_history')

def transaction_history(request):
    transactions = Transactions.objects.all()
    if (request.method == 'POST'):
        unique_id = request.POST['hidden_unique_id']
        user_query = Customers.objects.raw("SELECT * FROM home_customers where id='"+unique_id+"'")
        username = user_query[0].name
        transaction_single = Transactions.objects.raw("SELECT * FROM home_transactions WHERE reciever='"+username+"' OR sender='"+username+"'")
        return render(request, "home/transaction_history.html", {'transactions': transaction_single, 'username':"for "+username})
    return render(request, "home/transaction_history.html", {'transactions': transactions, 'username':''})