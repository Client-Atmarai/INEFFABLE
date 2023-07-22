from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse,HttpResponseRedirect
from .models import AdminLogin,ResgisterStudent
from django.core.exceptions import ObjectDoesNotExist
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from ineffable_app.models import ResgisterStudent,CentreRegisterStudent,Status_create,Studentform,CentreStatus,Student_form_creation
from django.contrib.auth.decorators import login_required 
import pandas as pd
import sqlite3
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.
def home(request):
    if request.method=='GET':
        resp=render(request,'index.html')    
        return resp
    elif request.method=="POST":
        if 'btnenq' in request.POST:
            resp=render(request,'enquiry.html')    
            return resp
        elif 'btnlog' in request.POST:
            resp=render(request,'adminAPP/index.html')    
            return resp    
        elif "btncenter" in request.POST:
              user=User.objects.all()
              resp=render(request,"adminAPP/search_centre.html",{'user':user})
              return resp
  
def about(request):    
    data=ResgisterStudent.objects.all()
    for a in data:
         print(a.first_name)
    if request.method=='GET':
            resp=render(request,'about.html') 
            return resp
    elif request.method=="POST":
            if 'btnenq' in request.POST:
                resp=render(request,'enquiry.html')    
                return resp
            elif 'btnlog' in request.POST:
                resp=render(request,'adminAPP/index.html')    
                return resp 
            elif "btncenter" in request.POST:
                user=User.objects.all()
                resp=render(request,"adminAPP/search_centre.html",{'user':user})
                return resp 

def notice(request):    
        if request.method=='GET':
            resp=render(request,'notice.html') 
            return resp
        elif request.method=="POST":
            if 'btnenq' in request.POST:
                 resp=render(request,'enquiry.html')    
                 return resp
            elif 'btnlog' in request.POST:
                 resp=render(request,'adminAPP/index.html')    
                 return resp  

def contact(request):    
        if request.method=='GET':
            resp=render(request,'contact.html') 
            return resp
        elif request.method=="POST":
              if 'btnenq' in request.POST:
                 resp=render(request,'enquiry.html')    
                 return resp
              elif 'btnlog' in request.POST:
                  resp=render(request,'adminAPP/index.html')    
                  return resp    
              elif "btncenter" in request.POST:
               user=User.objects.all()
               resp=render(request,"adminAPP/search_centre.html",{'user':user})
               return resp
  
          #   if 'btnenq' in request.POST:
          #        resp=render(request,'enquiry.html')    
          #        return resp
          #   elif 'btnlog' in request.POST:
          #        resp=render(request,'adminAPP/index.html')    
          #        return resp  

def enquiry(request):
    resp=render(request,'enquiry.html')    
    return resp

def enq_form(request):
   try: 
    srn=int(request.POST.get("txtrn",0))
    data=Student_form_creation.objects.filter(rollno=srn).all()
    data2=Status_create.objects.get(student_rollno=srn)
    stas=data2.status
    d1={'data':data,'status':stas}
    resp=render(request,"enquiry.html",context=d1)
    return resp
   except ObjectDoesNotExist:
        d={'msg':"not found at"}
        resp=render(request,"error.html",context=d)
        return resp
def search(request):
     return render(request,"adminAPP/search.html")
def searchcentre(request):
     if request.method=="GET":
          return render(request,"adminAPP/search.html")
     elif request.method=="POST":
          #centrecode=int(request.POST.get('centrecode',00))
          if "btn_submit" in request.POST:
                    centrecode=int(request.POST.get('centrecode',00))
                    data=CentreStatus.objects.filter(centrecode=centrecode).all()
                    data1=Student_form_creation.objects.filter(centre_code=centrecode).all()
                    d1={'data':data,'data1':data1} 
                    #print(data)
                    resp=render(request,'adminAPP/search.html',context=d1)
                    return resp      
          
          #   if CentreStatus.objects.filter(centrecode=centrecode).exists():
          #          data=CentreStatus.objects.get(centrecode=centrecode)
          #          print(data)
          #          d={'data':data}
          #      #     print(data)
          #          return render(request,"adminAPP/search.html",context=d)
          #   else:
          #          d={'msg':"Centrecode does not exist"}
          #          return render(request,"adminAPP/search.html",context=d)

              
def error(request):
     resp=render(request,"error.html")
     return resp


def registration(req):
     resp=render(req,'adminAPP/registration.html')
     return resp

def centre_registration(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        data=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        data.save()
        re=HttpResponse("User Created")
        return re
    resp=render(request,"adminAPP/centre_registration.html")
    return resp
def logout_student(request):     
     try: 
       logout(request)
       return redirect('')
     except ObjectDoesNotExist:
        return redirect('')


def centre_logout(request):
     logout(request)
     return redirect('')

def add_student(request):
     return render(request,"adminApp/Student_Register_form.html")

def stu_logout(request):
     logout(request)
     return render(request,"adminAPP/centre_login.html")

def stu_log(request):
     logout(request)
     return redirect('')
def admin_logout(request):
     logout(request)
     return redirect('index')

def sample(request):
     return render(request,"adminAPP/sample.html")
def status_check(request):
     tt=Studentform.objects.all()
     d={'tt':tt}   
     return render(request,"adminAPP/status_table.html",context=d)
def admin_check_status(request):
    s=Status_create()
    if request.method=="POST":
        #  if 'btn_accept' in request.POST:
          s.status=request.POST.get('status')
          s.student_rollno=request.POST.get('rollno')
          s.centre_name=request.POST.get('centre_code')
          s.save()
          if s.status=="accept":
                # d={'msg':"APPROVED"}
                # resp=render(request,"adminAPP/status_table.html",context=d)
                resp=HttpResponse("<h1>Approval</h1>")
                return resp
          elif  s.status=="reject" :
                #  d={'msg':"REJECTED"}
                #  resp=render(request,"adminAPP/status_table.html",context=d)
                  resp=HttpResponse("<h1>Rejected</h1>")
                  return resp
          res=render(request,"enquiry.html")
          return res
# center login
def  centre_login(request):
     if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            d={'user':user}
            return render(request,"adminAPP/form_centre.html",context=d)
     return render(request,"adminAPP/centre_login.html")

def StudentRegisterForm(request):
     resp=render(request,"adminAPP/Student_Register_Form.html")
     return resp
def centre_logout(request):
     logout(request)
     return redirect('')

"""Creation of Centre registration form"""
def create_centre_form(request):
     if request.method=="GET":
          return render(request,"AdminApp/Student_Register_form.html")
     elif request.method=="POST":
        if "btnregstu" in request.POST:
          crs=CentreRegisterStudent()
          crs.student_name=request.POST.get("txtstudentname","N/A")
          crs.mother_name=request.POST.get("txtmothername","N/A")
          crs.father_name=request.POST.get("txtfathername","N/A")
          crs.rollno=request.POST.get("txtrollno",0)
          crs.image=request.POST.files=request.FILES.get("txtphoto","N/A")
          crs.Dob=request.POST.get("txtdob","N/A")
          crs.centre_name=request.POST.get("txtcenter","N/A")
          crs.course_name=request.POST.get("txtcourse","N/A")
          crs.duration=request.POST.get("txtduration","n/a")
          crs.examheldon=request.POST.get("txtexam","N/A")
          crs.percent=request.POST.get("txtper",0)
          crs.grade=request.POST.get('txtgrade',"N/A")
          crs.session=request.POST.get("txtsession","N/A")
          crs.centre_code=request.POST.get("txtcentercode",0)
          crs.dateofissue=request.POST.get("txtissue","N/A")
          crs.remark=request.POST.get("txtremark","N/A")
          crs.mark_s1=request.POST.get("txtmarks_sub1",0)
          crs.mark_s2=request.POST.get("txtmarks_sub2",0)
          crs.mark_s3=request.POST.get("txtmarks_sub3",0)
          crs.mark_s4=request.POST.get("txtmarks_sub4",0)
          crs.mark_s5=request.POST.get("txtmarks_sub5",0)
          crs.written_mark=request.POST.get("txtwritten_marks",0)
          crs.practical_mark=request.POST.get("txtprac_marks",0)
          crs.assignment_mark=request.POST.get("txtassignment_marks",0)
          crs.viva_mark=request.POST.get("txtviva_marks",0)
          crs.save()
          return render(request,"adminApp/Student_Register_form.html")
        elif "btn_update" in request.POST:
             crs=CentreRegisterStudent()
             crs.rollno=int(request.POST.get("txtrollno",0))
             #print(crs.rollno)
            #  cc=CentreRegisterStudent.objects.filter(rollno=crs.rollno).exists()
            #  print(cc)
             if CentreRegisterStudent.objects.filter(rollno=crs.rollno).exists():
                   
                   crs.student_name=request.POST.get("txtstudentname","N/A")
                   crs.mother_name=request.POST.get("txtmothername","N/A")
                   crs.father_name=request.POST.get("txtfathername","N/A")
                   crs.rollno=request.POST.get("txtrollno",0)
                   crs.image=request.POST.files=request.FILES.get("txtphoto","N/A")
                   crs.Dob=request.POST.get("txtdob","N/A")
                   crs.centre_name=request.POST.get("txtcenter","N/A")
                   crs.course_name=request.POST.get("txtcourse","N/A")
                   crs.duration=request.POST.get("txtduration","n/a")
                   crs.examheldon=request.POST.get("txtexam","N/A")
                   crs.percent=request.POST.get("txtper",0)
                   crs.grade=request.POST.get('txtgrade',"N/A")
                   crs.session=request.POST.get("txtsession","N/A")
                   crs.centre_code=request.POST.get("txtcentercode",0)
                   crs.dateofissue=request.POST.get("txtissue","N/A")
                   crs.remark=request.POST.get("txtremark","N/A")
                   crs.mark_s1=request.POST.get("txtmarks_sub1",0)
                   crs.mark_s2=request.POST.get("txtmarks_sub2",0)
                   crs.mark_s3=request.POST.get("txtmarks_sub3",0)
                   crs.mark_s4=request.POST.get("txtmarks_sub4",0)
                   crs.mark_s5=request.POST.get("txtmarks_sub5",0)
                   crs.written_mark=request.POST.get("txtwritten_marks",0)
                   crs.practical_mark=request.POST.get("txtprac_marks",0)
                   crs.assignment_mark=request.POST.get("txtassignment_marks",0)
                   crs.viva_mark=request.POST.get("txtviva_marks",0)
                   crs.save()
                   rp=HttpResponse("<h1>Updated something</h1>")
                   return rp

def form_update(request):
     s=User.objects.all()
     d={'s':s}
     return render(request,"adminAPP/form_centre.html",context=d)
def stu_form(request):
     if request.method=="GET":
      return render(request,"adminAPP/form_centre.html")
     elif request.method=="POST":
          if "btn_insert" in request.POST:
               sf=Studentform()
               sf.name=request.POST.get("username","N/A")
               sf.rollno=int(request.POST.get("urollno",00))
               sf.image=request.POST.files=request.FILES.get("uphoto","N/A")
               sf.dob=request.POST.get("udob","N/A")
               sf.course_name=request.POST.get("ucoursename","N/A")
               sf.session=request.POST.get("usession","N/A")
               sf.percnt=int(request.POST.get("upercentage",00))
               sf.grade=request.POST.get("ugrade","N/A")
               sf.centre_code=request.POST.get("ucentrecode","N/A")
               sf.remark=request.POST.get("uremark","N/A")
               sf.sub1=int(request.POST.get("usub1",00))
               sf.sub2=int(request.POST.get("usub2",00))
               sf.sub3=int(request.POST.get("usub3",00))
               sf.sub4=int(request.POST.get("usub4",00))
               sf.sub5=int(request.POST.get("usub5",00))
               sf.wm=int(request.POST.get("uwm",00))
               sf.pm=int(request.POST.get("upm",00))
               sf.am=int(request.POST.get("uam",00))
               sf.vm=int(request.POST.get("uvm",00))
               sf.save()
               d={'msg':"User have been created"}
               res=render(request,"adminAPP/form_centre.html",context=d)
               return res
          elif "btn_update" in request.POST:
               sf=Studentform()
               sf.rollno=int(request.POST.get("urollno",0))
               # print(st.rollno)
               if Studentform.objects.filter(rollno=sf.rollno).exists():
                    sf.name=request.POST.get("username","N/A")
                    sf.rollno=int(request.POST.get("urollno",00))
                    sf.image=request.POST.files=request.FILES.get("uphoto","N/A")
                    sf.dob=request.POST.get("udob","N/A")
                    sf.course_name=request.POST.get("ucoursename","N/A")
                    sf.session=request.POST.get("usession","N/A")
                    sf.percnt=int(request.POST.get("upercentage",00))
                    sf.grade=request.POST.get("ugrade","N/A")
                    sf.centre_code=request.POST.get("ucentrecode","N/A")
                    sf.remark=request.POST.get("uremark","N/A")
                    sf.sub1=int(request.POST.get("usub1",00))
                    sf.sub2=int(request.POST.get("usub2",00))
                    sf.sub3=int(request.POST.get("usub3",00))
                    sf.sub4=int(request.POST.get("usub4",00))
                    sf.sub5=int(request.POST.get("usub5",00))
                    sf.wm=int(request.POST.get("uwm",00))
                    sf.pm=int(request.POST.get("upm",00))
                    sf.am=int(request.POST.get("uam",00))
                    sf.vm=int(request.POST.get("uvm",00))
                    sf.save()
                    d={'msg':"Roll number have been updated"}
                    res=render(request,"adminAPP/form_centre.html",context=d)
                    return res
          return render(request,"adminAPP/form_centre.html")





def courses(request):    
        if request.method=='GET':
            resp=render(request,'course.html') 
            return resp
        elif request.method=="POST":
              if 'btnenq' in request.POST:
                 resp=render(request,'enquiry.html')    
                 return resp
              elif 'btnlog' in request.POST:
                  resp=render(request,'adminAPP/index.html')    
                  return resp    
              elif "btncenter" in request.POST:
               user=User.objects.all()
               resp=render(request,"adminAPP/search_centre.html",{'user':user})
               return resp
  

def adduser(request):
     if request.method=="POST":
          if 'btnuser' in request.POST:
               res=render(request,'adminAPP/registration.html')
               return res
          elif 'btnlogout' in request.POST:
            res=render(request,'index.html')
            return res

def index(request):
    resp=render(request,"adminAPP/index.html")
    return resp

def hello(request):
    resp=render(request,"adminAPP/hello.html")
    return resp

def pdf_report(request):
     rep=render(request,"pdf_report.html",content_type="application/pdf")
     return rep

def pdf_creation(request,c_id):    
    re=Student_form_creation.objects.filter(rollno=c_id).all()
    template_path = 'pdf_report.html'
    context = {'re': re}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] =  'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response,show_error_page=True)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def validateuser(request):
    adminid=request.POST['email_id']
    password=request.POST['password']
    try:
       object=AdminLogin.objects.get(adminemail=adminid,adminpassword=password)
       if object is not None:
           request.session['adminemail']=adminid
           r=render(request,"adminAPP/registration.html")
           return r
    except ObjectDoesNotExist:
         resp=render(request,"adminAPP/index.html")
         return resp         
          
