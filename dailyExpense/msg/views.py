from django.shortcuts import render,HttpResponse
from django.contrib import messages as msg
def firstmethod(request):

    return render(request,'prc_home.html')

def rg(request):
    if request.method=='POST':
        id=request.POST.get('id')
        if int(id)==101:
            #msg.add_message(request,msg.INFO,"Same Form Display Aggain")
            #msg.add_message(request,msg.SUCCESS,"User Info registerd Successfully")
            msg.info(request,"Same Form Display Aggain")
            msg.success(request,"User Info registerd Successfully")
            return render(request,'table.html')
        else:
            #msg.add_message(request,msg.ERROR,"Please Fill Validate Content")
            msg.error(request,"Please Fill Validate Content")
            return render(request,'table.html')


    else:
        msg.add_message(request,msg.INFO,"This User REGISTRATION FROM")
        msg.add_message(request,msg.INFO,"Please Fill In Capital Letter")
        return render(request,'table.html')