from datetime import datetime
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


# Create your views here.
from myapp.models import *


def login_get(request):
    return render(request,"login.html")


def login_post(request):
    username = request.POST['username']
    password = request.POST['password']

    user=authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        if user.groups.filter(name='admin').exists():
            messages.success(request,'login successfully')
            return redirect('/myapp/admin_home/')
        elif user.groups.filter(name='Lab assistant').exists():
            messages.success(request, 'login successfully')
            return redirect('/myapp/labassist_index_get/')
        elif user.groups.filter(name='Staff').exists():
            messages.success(request, 'login successfully')
            return redirect('/myapp/staff_index/')

        else:
            messages.success(request, 'invalid user')
            return redirect('/myapp/login_get/')

    else:
        messages.success(request, 'invalid user')
        return redirect('/myapp/login_get/')


def staff_index(request):
    return render(request,'staffpage/Staff_index.html')





def admin_home(request):
    return render(request,"adminpage/admin_index.html")


def admin_changepassword_get(request):
    return render(request,"adminpage/admin_change_password.html")

def admin_changepassword_post(request):
    old_pass = request.POST['old_pass']
    new_pass = request.POST['new_pass']
    confirm_pass = request.POST['confirm_pass']

    user= request.user
    a = check_password(old_pass,request.user.password)
    if a:
        if new_pass==confirm_pass:
            user=request.user
            user.set_password(confirm_pass)
            user.save()
            logout(request)
            return redirect("/myapp/login_get/")
        else:
            messages.warning(request,"password does not match")
            return redirect("/myapp/admin_changepassword_get/")
    else:
        messages.warning(request,"invalid password")
        return redirect("/myapp/admin_changepassword_get/")


#add course
def admin_addcourse_get(request):
    data=Departement.objects.all()
    return render(request, "adminpage/add_course.html",{'data':data})


def admin_add_course_post(request):
    course = request.POST['course']
    totsem = request.POST['totsem']
    did=request.POST['dept']

    a=Course()
    a.coursename=course
    a.totelsem=totsem
    a.DEP=Departement.objects.get(id=did)
    a.save()
    return redirect('/myapp/admin_viewcourse_get/')


def admin_editcourse_get(request,id):
    data=Departement.objects.all()
    data1=Course.objects.get(id=id)
    return render(request, "adminpage/edit_course.html",{'data':data,'data1':data1})


def admin_editcourse_post(request):
    course = request.POST['course']
    totsem = request.POST['totsem']
    did = request.POST['dept']
    id=request.POST['id']

    a = Course.objects.get(id=id)
    a.coursename = course
    a.totelsem = totsem
    a.DEP = Departement.objects.get(id=did)
    a.save()
    return redirect('/myapp/admin_viewcourse_get/')


def admin_delete_course(request,id):
    Course.objects.get(id=id).delete()
    return redirect('/myapp/admin_viewcourse_get/')



#add department

def admin_add_department_get(request):
    return render(request, "adminpage/add_department.html")


def admin_add_department_post(request):
    dept = request.POST['dept']

    a=Departement()
    a.departementname=dept
    a.save()
    a.save()
    return redirect('/myapp/admin_viewdepartment_get/')

def admin_editdepartment_get(request,id):
    data=Departement.objects.get(id=id)
    return render(request, "adminpage/edit_department.html",{'data':data})


def admin_editdepartment_post(request):
    dept = request.POST['dept']
    id=request.POST['id']

    a = Departement.objects.get(id=id)
    a.departementname = dept
    a.save()
    return redirect('/myapp/admin_viewdepartment_get/')


def admin_delete_department(request,id):
    Departement.objects.get(id=id).delete()
    return redirect('/myapp/admin_viewdepartment_get/')



#add lab
def admin_addlab_get(request):
    return render(request, "adminpage/add_lab.html")


def admin_addlab_post(request):
    lab=request.POST['labname']
    labno=request.POST['labno']

    a=Lab()
    a.labname=lab
    a.labno=labno
    a.save()
    return redirect('/myapp/admin_viewlab_get/')

def admin_editlab_get(request,id):
    data=Lab.objects.get(id=id)
    return render(request, "adminpage/edit_lab.html",{'data':data})

def admin_editlab_post(request):
    id=request.POST['id']
    lab=request.POST['labname']
    labno=request.POST['labno']

    a=Lab.objects.get(id=id)
    a.labname=lab
    a.labno=labno
    a.save()
    return redirect('/myapp/admin_viewlab_get/')


def admin_deletelab(request,id):
    Lab.objects.get(id=id).delete()
    return redirect('/myapp/admin_viewlab_get/')


#add lab assistant
def admin_addlabassist_get(request):
    return render(request, "adminpage/add_labassist.html")


def admin_addlabassist_post(request):
    labassistantname=request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    gender = request.POST['gender']
    place = request.POST['place']
    dob = request.POST['dob']
    city = request.POST['city']
    state = request.POST['state']
    pincode = request.POST['pincode']

    if User.objects.filter(username=email).exists():
        messages.warning(request,'already exist')
    else:


        user = User.objects.create_user(username=email, password=phone)
        user.groups.add(Group.objects.get(name='Lab assistant'))
        user.save()


        a=Labassistant()
        a.labassistantname=labassistantname
        a.email = email
        a.phone = phone
        a.gender = gender
        a.dob=dob
        a.place = place
        a.city = city
        a.state = state
        a.pincode = pincode
        a.USER=user
        a.save()
        return redirect('/myapp/admin_viewlabassist_get/')


def admin_editlabassist_get(request,id):
    data=Labassistant.objects.get(id=id)

    return render(request, "adminpage/edit_labassist.html",{'data':data})



def admin_editlabassist_post(request):
    labassistantname=request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    gender = request.POST['gender']
    place = request.POST['place']
    dob = request.POST['dob']
    city = request.POST['city']
    state = request.POST['state']
    pincode = request.POST['pincode']
    id=request.POST['id']

    a=Labassistant.objects.get(id=id)
    a.labassistantname=labassistantname
    a.email = email
    a.phone = phone
    a.gender = gender
    a.dob=dob
    a.place = place
    a.city = city
    a.state = state
    a.pincode = pincode
    a.save()
    return redirect('/myapp/admin_viewlabassist_get/')

def admin_deletelabassist_get(request, id):
    Labassistant.objects.get(USER_id=id).delete()
    User.objects.get(id=id).delete()
    return redirect('/myapp/admin_viewlabassist_get/')


#add lab sub
def admin_addlabsub_get(request):
    return render(request, "adminpage/add_labsub.html")


def admin_addlabsub_post(request):
    sub=request.POST['sub']

    a=Labsubject()
    a.subject=sub
    a.save()
    return redirect("/myapp/admin_viewlabsub_get/")

def admin_editlabsub_get(request,id):
    data=Labsubject.objects.get(id=id)
    return render(request, "adminpage/edit_labsub.html",{'data':data})


def admin_editlabsub_post(request):
    sub = request.POST['sub']
    id=request.POST['id']

    a = Labsubject.objects.get(id=id)
    a.subject = sub
    a.save()
    return redirect("/myapp/admin_viewlabsub_get/")


def admin_delete_labsub(request,id):
    Labsubject.objects.get(id=id).delete()
    return redirect("/myapp/admin_viewlabsub_get/")



#add labsub schedule
def admin_addlabsub_schedule_get(request):
    lab=Laballocation.objects.all()
    course=Course.objects.all()
    sub=Labsubject.objects.all()

    return render(request, "adminpage/add_labsub_schedule.html",{'lab':lab,'course':course,'labsub':sub})


def admin_addlabsub_schedule_post(request):
    lab=request.POST['lab']
    course=request.POST['course']
    sub=request.POST['sub']
    day=request.POST['day']
    from_=request.POST['from']
    to=request.POST['to']
    sem=request.POST['sem']

    a=Labsubjectschedule()
    a.day=day
    a.fromtime=from_
    a.totime=to
    a.LABSUB_id=sub
    a.LABALLOCATION_id=lab
    a.save()

    return redirect('/myapp/admin_viewlabsub_schedule_get/')


def admin_editlab_schedule_get(request,id):
    lab=Laballocation.objects.all()
    course=Course.objects.all()
    sub=Labsubject.objects.all()
    data=Labsubjectschedule.objects.get(id=id)

    return render(request, "adminpage/edit_labsub_schedule.html",{'lab':lab,'course':course,'labsub':sub,'data':data})




def admin_editlab_schedule_post(request):
    lab = request.POST['lab']
    course = request.POST['course']
    sub = request.POST['sub']
    day = request.POST['day']
    from_ = request.POST['from']
    to = request.POST['to']
    sem = request.POST['sem']
    id=request.POST['id']

    a = Labsubjectschedule.objects.get(id=id)
    a.day = day
    a.fromtime = from_
    a.totime = to
    a.LABSUB_id = sub
    a.LABALLOCATION_id = lab
    a.save()

    return redirect('/myapp/admin_viewlabsub_schedule_get/')



def admin_viewlabsub_schedule_get(request):
    data=Labsubjectschedule.objects.all()
    return render(request, "adminpage/view_labsub_schedule.html",{'data':data})


def admin_deletelabsub_schedule_get(request,id):
    Labsubjectschedule.objects.get(id=id).delete()
    return redirect('/myapp/admin_viewlabsub_schedule_get/')


def admin_viewlabsub_schedule_post(request):
    return

#add staff
def admin_addstaff_get(request):
    return render(request, "adminpage/add_staff.html")


def admin_addstaff_post(request):
    staffname=request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    gender = request.POST['gender']
    place = request.POST['place']
    city = request.POST['city']
    dob = request.POST['dob']
    state = request.POST['state']
    pincode = request.POST['pincode']


    if User.objects.filter(username=email).exists():
        messages.warning(request,'already exist')
    else:

        user = User.objects.create_user(username=email, password=phone)
        user.groups.add(Group.objects.get(name='Staff'))
        user.save()


        a=Staff()
        a.staffname=staffname
        a.email = email
        a.phone = phone
        a.gender = gender
        a.place = place
        a.city = city
        a.state = state
        a.pincode = pincode
        a.USER=user
        a.dob=dob
        a.save()

        return redirect('/myapp/admin_viewstaff_get')


def admin_editstaff_get(request,id):
    data=Staff.objects.get(id=id)

    return render(request, "adminpage/edit_staff.html",{'data':data})




def admin_editstaff_post(request):
    staffname = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    gender = request.POST['gender']
    place = request.POST['place']
    city = request.POST['city']
    dob = request.POST['dob']
    state = request.POST['state']
    pincode = request.POST['pincode']
    id=request.POST['id']



    a = Staff.objects.get(id=id)
    a.staffname = staffname
    a.email = email
    a.phone = phone
    a.gender = gender
    a.place = place
    a.city = city
    a.state = state
    a.pincode = pincode
    a.dob = dob
    a.save()

    return redirect('/myapp/admin_viewstaff_get')

def admin_deletestaff_get(request, id):
    Staff.objects.get(USER_id=id).delete()
    User.objects.get(id=id).delete()
    return redirect('/myapp/admin_viewstaff_get')



#add student

def admin_addstudent_get(request):
    data=Course.objects.all()
    return render(request, "adminpage/add_student.html",{'data':data})


def admin_addstudent_post(request):
    studentname=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    dob=request.POST['dob']
    gender=request.POST['gender']
    place=request.POST['place']
    city=request.POST['city']
    state=request.POST['state']
    pincode=request.POST['pincode']
    photo=request.FILES['photo']

    cid=request.POST['cid']

    if User.objects.filter(username=email).exists():
        messages.warning(request,'already exist')
    else:
        fs=FileSystemStorage()
        date=datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
        fs.save(date, photo)
        path=fs.url(date)


        user=User.objects.create_user(username=email, password=phone)
        user.groups.add(Group.objects.get(name='Student'))
        user.save()


        a=Student()
        a.studentname=studentname
        a.email=email
        a.phone=phone
        a.dob=dob
        a.gender=gender
        a.place=place
        a.city=city
        a.state=state
        a.pincode=pincode
        a.photo=path
        a.COURSE=Course.objects.get(id=cid)
        a.save()
    return redirect('/myapp/admin_viewstudent_get/')


def admin_editstudent_get(request,id):
    data=Student.objects.get(id=id)
    data1=Course.objects.all()
    return render(request, "adminpage/edit_student.html",{'data':data,'data1':data1})

def admin_deletestudent_get(request,id):
    Student.objects.get(id=id).delete()
    # User.objects.get(id=id).delete()
    return redirect("/myapp/admin_viewstudent_get")

def admin_editstudent_post(request):
    studentname = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    dob = request.POST['dob']
    gender = request.POST['gender']
    place = request.POST['place']
    city = request.POST['city']
    state = request.POST['state']
    pincode = request.POST['pincode']

    cid = request.POST['cid']
    id=request.POST['id']

    a = Student.objects.get(id=id)



    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        date = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        fs.save(date, photo)
        path = fs.url(date)
        a.photo = path
        a.save()


    a.studentname = studentname
    a.email = email
    a.phone = phone
    a.dob = dob
    a.gender = gender
    a.place = place
    a.city = city
    a.state = state
    a.pincode = pincode
    a.COURSE = Course.objects.get(id=cid)
    a.save()
    return redirect('/myapp/admin_viewstudent_get/')





#add   assist allocation
def admin_assistallocation_get(request):
    data=Lab.objects.all()
    data1=Labassistant.objects.all()
    return render(request, 'adminpage/assist_allocation.html',{'data':data,'data1':data1})


def admin_assistallocation_post(request):
    labname=request.POST['labs']
    labassistantname=request.POST['labassist']


    a=Laballocation()
    a.date = datetime.now().today()
    a.status='pending'
    a.LAB=Lab.objects.get(id=labname)
    a.LABASSIST=Labassistant.objects.get(id=labassistantname)
    a.save()

    return redirect('/myapp/admin_viewassist_allocation_get/')


def admin_editassistallocation_get(request,id):
    data=Lab.objects.all()
    data1=Labassistant.objects.all()
    data2=Laballocation.objects.get(id=id)
    return render(request, "adminpage/edit_assist_allocation.html",{'data':data,'data1':data1,'data2':data2})


def admin_editassistallocation_post(request):
    labname = request.POST['labs']
    labassistantname = request.POST['labassist']
    id=request.POST['id']

    a = Laballocation.objects.get(id=id)
    a.date = datetime.now().today()
    a.status = 'pending'
    a.LAB = Lab.objects.get(id=labname)
    a.LABASSIST = Labassistant.objects.get(id=labassistantname)
    a.save()

    return redirect('/myapp/admin_viewassist_allocation_get/')

def admin_deleteassistallocation_post(request,id):
    Laballocation.objects.get(id=id).delete()
    return redirect('/myapp/admin_viewassist_allocation_get/')

def admin_viewassist_allocation_get(request):
    data=Laballocation.objects.all()
    return render(request,"adminpage/view_assist_allocation.html",{'data':data})


#staff sub allocation
def admin_staffsuballoc_get(request):
    data=Staff.objects.all()
    data1=Labsubject.objects.all()

    return render(request,"adminpage/admin_staff_sub_alloc.html",{'data':data,'data1':data1})

def admin_staffsuballoc_post(request):
    staff=request.POST['staff']
    subject=request.POST['subject']
    a=Labsuballocation()
    a.date=datetime.now().today()
    a.status='allocated'
    a.LABSUB=Labsubject.objects.get(id=subject)
    a.STAFF=Staff.objects.get(id=staff)
    a.save()


    return redirect('/myapp/admin_viewsuballoc/')


def admin_edit_staffsuballoc_get(request,id):
    data=Staff.objects.all()
    data1=Labsubject.objects.all()
    data2=Labsuballocation.objects.get(id=id)
    return render(request,"adminpage/admin_edit_staffsub_alloc.html",{'data':data,'data1':data1,'data2':data2})

def admin_edit_staffsuballoc_post(request):
    staff=request.POST['staff']
    subject=request.POST['subject']
    id=request.POST['id']
    a=Labsuballocation.objects.get(id=id)
    a.date=datetime.now().today()
    a.LABSUB_id=subject
    a.STAFF_id=staff
    a.save()


    return redirect('/myapp/admin_viewsuballoc/')

def admin_delete_staffsuballoc(request,id):
    Labsuballocation.objects.get(id=id).delete()
    return redirect('/myapp/admin_viewsuballoc/')


def admin_viewsuballoc(request):
    data=Labsuballocation.objects.all()
    return render(request,'adminpage/view_staff_sub_allocation.html',{'data':data})

#start of view functions of admin module

#view course
def admin_viewcourse_get(request):
    data=Course.objects.all()

    return render(request, "adminpage/view_course.html",{'data':data})


def admin_viewcourse_post(request):
    return

#view department
def admin_viewdepartment_get(request):
    data=Departement.objects.all()
    return render(request, "adminpage/view_department.html",{'data':data})



def admin_viewdepartment_post(request):
    return

#view lab
def admin_viewlab_get(request):
    data=Lab.objects.all()
    return render(request, "adminpage/view_lab.html",{'data':data})


def admin_viewlab_post(request):
    return


#view lab assistant
def admin_viewlabassist_get(request):
    data=Labassistant.objects.all()
    return render(request, "adminpage/view_labassist.html",{'data':data})


def admin_viewlabassist_post(request):
    return


#view labsub
def admin_viewlabsub_get(request):
    data=Labsubject.objects.all()
    return render(request, "adminpage/view_labsub.html",{'data':data})


def admin_viewlabsub_post(request):
    return


#view labsub schedule



#view staff
def admin_viewstaff_get(request):
    data=Staff.objects.all()
    return render(request, "adminpage/view_staff.html",{'data':data})


def admin_viewstaff_post(request):
    return

#view student
def admin_viewstudent_get(request):
    data=Student.objects.all()
    return render(request, "adminpage/view_student.html",{'data':data})


def admin_viewstudent_post(request):
    return




def admin_blockedapps_get(request):
    return render(request, "adminpage/blocked_apps.html")


def admin_blockedapps_post(request):
    return

#view attendance report
def admin_viewattendance_report_get(request):
    return render(request, "adminpage/view_attendance_report.html")


def admin_viewstaff_suballoc_get(request):
    return render(request, "adminpage/view_staff_sub_allocation.html")




#ending of admin module








#lab assistant module





def labassist_index_get(request):
    return render(request,"labassistpage/labassist_index.html")


def labassist_addsys_healthreport_get(request):
    data = System.objects.all()
    return render(request,"labassistpage/labassist_add_sys_health_rep.html",{'data':data})

def labassist_addsys_healthreport_post(request):
    sid=request.POST['system']
    message=request.POST['message']


    h=Healthreport()
    h.SYSTEM_id=sid
    h.problem=message
    h.solvedstatus="pending"
    h.date=datetime.now()
    h.time=datetime.now().time()
    h.save()
    return redirect('/myapp/labassist_addsys_healthreport_get/')


#add system
def labassist_addsystem_get(request):
    data=Lab.objects.all()
    return render(request, "labassistpage/add_system.html",{'data':data})


def labassist_addsystem_post(request):
    systemno=request.POST['systemno']
    macaddress=request.POST['macaddress']

    l=Laballocation.objects.get(LABASSIST__USER_id=request.user)

    a=System()
    a.systemno=systemno
    a.macaddress=macaddress
    a.LAB_id=l.LAB.id
    a.save()
    return redirect('/myapp/labassist_viewsystem_get/')


def labassist_editsystem_get(request,id):
    data= System.objects.get(id=id)
    data2=Lab.objects.all()
    return render(request, "labassistpage/edit_system.html",{'data':data,'data2':data2})


def labassist_editsystem_post(request):
    systemno = request.POST['systemno']
    macaddress = request.POST['macaddress']
    id = request.POST['id']

    a = System.objects.get(id=id)
    a.systemno = systemno
    a.macaddress = macaddress
    a.save()
    return redirect('/myapp/labassist_viewsystem_get/')



def labassist_deletesystem_get(request,id):
    System.objects.get(id=id).delete()
    return redirect('/myapp/labassist_viewsystem_get/')

#view system
def labassist_viewsystem_get(request):
    data = System.objects.all()
    return render(request, "labassistpage/view_system.html", {'data': data})




def labassist_allocatesys_student_get(request):
    s=Laballocation.objects.get(LABASSIST__USER_id=request.user)
    student=Student.objects.all()
    system=System.objects.filter(LAB=s.LAB.id)
    return render(request,"labassistpage/labassist_allocate_sys_student.html",{'student':student,'system':system})

def labassist_allocatesys_student_post(request):
    student=request.POST['student']
    system=request.POST['system']

    a=Systemallocation()
    a.SYSTEM_id=system
    a.STUDENT_id=student
    a.date=datetime.now().date()
    a.status='pending'
    a.save()

    return redirect('/myapp/labassist_view_sys_allocation_get/')





def labassist_view_alloc_lab_get(request):
    data=Laballocation.objects.filter(LABASSIST__USER_id=request.user)
    return render(request,"labassistpage/labassist_view_allocated_labs.html",{'data':data})

def labassist_view_profile_get(request):
    data=Labassistant.objects.get(USER_id=request.user)
    return render(request,"labassistpage/labassist_view_profile.html",{'data':data})

def labassist_view_sys_allocation_get(request):
    s=Laballocation.objects.get(LABASSIST__USER_id=request.user)
    data=Systemallocation.objects.filter(SYSTEM__LAB=s.LAB.id)
    return render(request, "labassistpage/labassist_view_sys_allocation.html",{'data':data})

def labassist_delete_sys_allocation_get(request,id):
    Systemallocation.objects.get(id=id).delete()
    return  redirect('/myapp/labassist_view_sys_allocation_get/#abc')


def labassist_view_sys_healthreport_get(request):
    data=Healthreport.objects.all()
    return render(request, "labassistpage/labassist_view_sys_health_reports.html",{'data':data})



def labassist_syst_monitor_get(request):
    data = System.objects.all()
    return render(request,"labassistpage/labassist_system_monitor.html",{'data':data})

def labassist_syst_monitor_post(request):
    return

def labassist_view_filelogs_get(request,id):
    data=Filelogs.objects.filter(id=id)
    return render(request,"labassistpage/labassist_view_file_logs.html",{'data':data})


def labassist_view_processlogs_get(request,id):
    data=ProcessLogs.objects.filter(id=id)
    return render(request,"labassistpage/labassist_view_process_logs.html",{'data':data})

def labassist_view_keylogs_get(request,id):
    data = Keylogs.objects.filter(id=id)
    return render(request,"labassistpage/labassist_view_key_logs.html",{'data':data})


def labassist_command_invocation_get(request, id):
    return render(request,"labassistpage/labassist_command_invocation.html")

def labassist_command_invocation_post(request):
    command=request.POST['command']
    a=Command()
    a.date=datetime.now().today()
    a.time=datetime.now().time()
    a.status='pending'
    a.STAFF=request.user
    a.save()
    return redirect('/myapp/labassist_command_invocation_get/')


def labassist_view_scrnshot_get(request,id):
    data=Screenshots.objects.all()
    return  render(request,"labassistpage/labassist_view_screenshot.html",{'data':data})

#ending of labassist module






#staff module


def staff_command_invoc_get(request):
    return render(request, "staffpage/staff_command_invocation.html")

def staff_command_invoc_post(request):
    return

def staff_helpreq_get(request):
    return render(request, "staffpage/staff_help_req.html")

def staff_helpreq_post(request):
    return

def staff_sentreply_get(request):
    return render(request, "staffpage/staff_sent_replies.html")

def staff_sentreply_post(request):
    return

def staff_systmonitor_get(request):
    return render(request, "staffpage/staff_system_monitor.html")

def staff_systmonitor_post(request):
    return


def staff_viewstud_complaint_get(request):
    return  render(request,"staffpage/staff_view_student_complaint.html")

def staff_view_profile_get(request):
    d=request.user
    data=Staff.objects.get(USER_id=d)
    return render(request,"staffpage/staff_view_profile.html",{'data':data})



def staff_view_system_get(request):
    return render(request,"staffpage/staff_view_system.html")


def staff_view_alloc_sub_get(request):
    d=request.user
    data=Labsuballocation.objects.filter(STAFF__USER_id=d)
    return render(request,"staffpage/staff_view_allocated_subject.html",{'data':data})



def staff_view_filelogs_get(request):
    return render(request,"staffpage/staff_view_file_logs.html")

def staff_view_keylogs_get(request):
    return render(request,"staffpage/staff_view_key_logs.html")


def staff_view_processlogs_get(request):
    return render(request,"staffpage/staff_view_process_logs.html")


def staff_view_scrnshot_get(request):
    return render(request,"staffpage/staff_view_screenshot.html")


def staff_view_attendance_get(request):
    return render(request,"staffpage/staff_view_attendance.html")




