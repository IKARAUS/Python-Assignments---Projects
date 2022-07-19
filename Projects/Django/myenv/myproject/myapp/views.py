from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models  import *


# Create your views here.

def home(request):

    if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        if uid.role=="Chairman":
            cid = chairman.objects.get(user_id = uid)

            context={
                "uid":uid,
                "cid":cid,
            }
            return render(request,'myapp/index.html',context)
        else:
            pass
    else:
        return render(request,'myapp/login.html')


def login(request):
    if "email" in request.session:
        return redirect("home")

    if request.POST:
        p_email = request.POST['email']   # p_email is python variable /////  email is HTML variable # 
        p_password = request.POST['password']

        try:
            uid=user.objects.get(email = p_email)
            if uid.password == p_password:
                cid = chairman.objects.get(user_id = uid)
                print("---> firstname =",cid.firstname)
                request.session["email"]=p_email
                
                context={
                    "uid":uid,
                    "cid":cid,
                }
                return render(request,"myapp/index.html",context)
            else:
                context={
                    "e_msg":"INVALID PASSWORD"
                }
                return render(request,"myapp/login.html",context)

        except Exception as e:
            print("--->exception",e)
            context={
                "e_msg":"INVALID EMAIL ADDRESS"
             }
            return render(request,"myapp/login.html",context)
        
        # except user.DoesNotExist:
        #      print(" User Does Not Exist here")
        #      return render(request,"myapp/login.html")


        # print("----> Email", p_email)
        # print("--->Password",p_password)
        
    else:
        print("---> Page Just Loaded")
        return render(request,'myapp/login.html')

def doctor(request):
    
    return render(request,'myapp/doctor.html')




def logout(request):
    if "email" in request.session:
        del request.session["email"]
        return render(request,'myapp/login.html')
    else:
        return render(request,'myapp/login.html')


def profile(request):
    if "email" in request.session:
        uid=user.objects.get(email=request.session['email'])
        
        if uid.role=="chairman":
            cid=chairman.objects.get(user_id=uid)
            context={
                "uid":uid,
                "cid":cid,
            }

            return render(request,'myapp/profile.html',context)


def change_password(request):
    if 'email' in request.session:


        if request.POST:
            currentpassword=request.POST['currentpassword']
            new_password=request.POST['new_password']

            uid=user.objects.get(email=request.session['email'])
            cid=chairman.objects.get(user_id=uid)

            if uid.password == currentpassword:
                uid.password=new_password
                uid.save()

                context={
                    'uid':uid,
                    'cid':cid,
                    'msg':"Successfully password reset"
                }
                return render(request,'myapp/profile.html',context)

            else:
                cid=chairman.objects.get(user_id=uid)
                context={
                "uid":uid,
                "cid":cid,
                'msg':" INVALID PASSWORD "
            }
            return render(request,'myapp/profile.html',context)
        else:
            return redirect("login")

def edit_profile(request):
    if request.POST:
        uid=user.objects.get(email=request.session['email'])
       

        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        contact=request.POST['contact']
        block_no=request.POST['block_no']
        house_no=request.POST['house_no']
        about_me=request.POST['about_me']
        pic =request.FILES['pic']
        
        cid=chairman.objects.get(user_id=uid)
        if cid:
            cid.firstname=firstname
            cid.lastname=lastname
            cid.contact=contact
            cid.block_no=block_no
            cid.house_no=house_no
            cid.about_me=about_me
            if "pic" in request.FILES:
                cid.pic=pic
                cid.save()
            context={
                'uid':uid,
                'cid':cid,
            }

            return render(request, 'myapp/profile.html',context)
        else:
            print("Chairman not found")
            return redirect("profile")
    else:
        print("DATA not found")
        return redirect("login")
    

def add_notice(request):
        
    return render(request,'myapp/Add-Notice.html')


