from django.shortcuts import render,HttpResponse # type: ignore
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    return render(request,'index.html')

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def result(request):
    
    if request.method=="POST":
        name_id = request.POST.get('name_id')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        contact = Contact(name_id=name_id,fname=fname,lname=lname)
        contact.save()
        messages.success(request, "Your message has been send .")
        messages.success(request, "Your form filled succesfully.")
        full_name = fname + lname
        # return render(request,"result.html",{'name_id':name_id,'full_name':full_name})
        return render(request,"index.html")

    return render(request,'index.html')