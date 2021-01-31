from django.shortcuts import render, redirect ,HttpResponse
from .forms import user_form,Income_form,Expense_form, Login_form
from .models import userRegister,User, Income, Expense
from django.contrib.auth import login as dj_login, logout as dj_logout ,authenticate

# Create your views here.
def home(request):    
    return render(request,'home_before_login.html')

def homepage(request):
    id=request.session.get('uid')
    bal=totalBalance(id)
    return render(request,'home.html',{'bal':bal})

def register(request):
    if request.method == "POST":
        s = user_form(request.POST)
        s.save()
        return redirect('/')
    else:        
        return render(request,'form.html',{'form': user_form, 'name':'user'})

def add_income(request):
    if request.method == "POST":
        s = Income_form(request.POST)
        s.save()
        return redirect('/')
    else:        
        return render(request,'form.html',{'form': Income_form, 'name':'Income'})

def add_expense(request):
    id=request.session.get('uid')
    bal=totalBalance(id)
    if request.method == "POST":
        s = Expense_form(request.POST)
        sp=request.POST.get('expense')
        if bal>int(sp):
            s.save()
            return redirect('/')
        else:
            expm="Your Expense Amount is Greater Than Balance"        
            return render(request,'form.html',{'form': Expense_form, 'name':'expense','expm':expm})
    else:
        expm="Your Expense Amount is Greater Then Balance"        
        return render(request,'form.html',{'form': Expense_form, 'name':'Expense'})

def income_list(request):
    uid=request.session.get('uid')
    objects=Income.objects.filter(user_id=uid)
    return render(request, 'income_list.html', {'objects':objects})

def expense_list(request):
    uid=request.session.get('uid')
    objects=Expense.objects.filter(user_id=uid)
    return render(request, 'expense_list.html', {'objects':objects})

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            dj_login(request,user)
            request.session['uid']=user.id
            id=request.session.get('uid')
            bal=totalBalance(id)
            return render(request,'home.html',{'bal':bal, 'user':user})
            
            #return redirect('home')
        else:
            lmsg="invalid username and password"
            d = {'form':Login_form, 'lmsg':lmsg, "name":"login" }
            return render(request,'form.html',d)
    else: 
        return render(request,'form.html', {'form':Login_form , "name":"login"})

def logout(request):
    dj_logout(request)
    return redirect('/')

def delete_income(request,id):
    inc=Income.objects.get(id=id)
    inc.delete()
    return redirect('/')

def delete_expense(request,id):
    exp=Expense.objects.get(id=id)
    exp.delete()
    return redirect('/')

def update_income(request, id):
    inc = Income.objects.get(id=id)  
    if request.method=='POST':
        f=Income_form(request.POST,instance=inc)
        f.save()
        return redirect('/Income_list')
    else:
        f=Income_form(instance=inc)
        return render(request,'form.html',{'form':f, "name":"Update"})

def totalBalance(id):
    elist=Expense.objects.filter(user_id=id)
    ilist=Income.objects.filter(user_id=id)
    totalIncome=0
    for i in ilist:
        totalIncome=totalIncome+i.income

    totalExpense=0
    for i in elist:
        totalExpense=totalExpense+i.expense
    
    return totalIncome-totalExpense

def edit_profile(request):
    id=request.session.get('uid')
    usr=UserInfo.objects.get(id=id)
    if request.method=='POST':
        f=UserForm(request.POST,instance=usr)
        f.save()
        return redirect('/')
    else:
        f=UserForm(instance=usr)
        return render(request,'form.html',{'form':f})

'''
    doubts
    ----------------
    1) add bootstrap class to forms
    2) rreturn redirect('home)
'''
      
    
