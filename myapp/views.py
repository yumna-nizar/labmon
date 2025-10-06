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
        else:
            messages.success(request, 'invalid user')
            return redirect('/myapp/login_get/')

    else:
        messages.success(request, 'invalid user')
        return redirect('/myapp/login_get/')


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





def admin_add_department_get(request):
    return render(request, "adminpage/add_department.html")


def admin_add_department_post(request):
    dept = request.POST['dept']

    a=Departement()
    a.departementname=dept
    a.save()
    a.save()
    return redirect('/myapp/admin_viewdepartment_get/')


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


def admin_addlabassist_get(request):
    return render(request, "adminpage/add_labassist.html")


def admin_addlabassist_post(request):
    return


def admin_addlabsub_get(request):
    return render(request, "adminpage/add_labsub.html")


def admin_addlabsub_post(request):
    sub=request.POST['sub']

    a=Labsubject()
    a.subject=sub
    a.save()
    return redirect("/myapp/admin_viewlabsub_get/")


def admin_addlabsub_schedule_get(request):
    return render(request, "adminpage/add_labsub_schedule.html")


def admin_addlabsub_schedule_post(request):
    return


def admin_addstaff_get(request):
    return render(request, "adminpage/add_staff.html")


def admin_addstaff_post(request):
    return


def admin_addstudent_get(request):
    data=Course.objects.all()
    return render(request, "adminpage/add_student.html",{'data':data})


def admin_addstudent_post(request):
    studentname=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    gender=request.POST['gender']
    place=request.POST['place']
    city=request.POST['city']
    state=request.POST['state']
    pincode=request.POST['pincode']
    photo=request.FILES['photo']

    if User.groups.filter(username=email).exists():
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
        a.gender=gender
        a.place=place
        a.city=city
        a.state=state
        a.pincode=pincode
        a.photo=path
        a.COURSE=cid


    return redirect('/myapp/admin_viewstudent_get/')


def admin_addsystem_get(request):
    return render(request, "adminpage/add_system.html")


def admin_addsystem_post(request):
    return


def admin_assistallocation_get(request):
    return render(request, 'adminpage/assist_allocation.html')


def admin_assistallocation_post(request):
    return


def admin_editassistallocation_get(request):
    return render(request, "adminpage/edit_assist_allocation.html")


def admin_editassistallocation_post(request):
    return


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

def admin_editlabassist_get(request):
    return render(request, "adminpage/edit_labassist.html")


def admin_editlabassist_post(request):
    return


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


def admin_editlab_schedule_get(request):
    return render(request, "adminpage/edit_labsub_schedule.html")


def admin_editlab_schedule_post(request):
    return


def admin_editstaff_get(request):
    return render(request, "adminpage/edit_staff.html")


def admin_editstaff_post(request):
    return


def admin_editstudent_get(request):
    return render(request, "adminpage/edit_student.html")


def admin_editstudent_post(request):
    return


def admin_editsystem_get(request):
    return render(request, "adminpage/edit_system.html")


def admin_editsystem_post(request):
    return


def admin_viewassist_allocation_get(request):
    return render(request, "adminpage/view_assist_allocation.html")


def admin_viewassist_allocation_post(request):
    return


def admin_viewcourse_get(request):
    data=Course.objects.all()

    return render(request, "adminpage/view_course.html",{'data':data})


def admin_viewcourse_post(request):
    return


def admin_viewdepartment_get(request):
    data=Departement.objects.all()
    return render(request, "adminpage/view_department.html",{'data':data})



def admin_viewdepartment_post(request):
    return


def admin_viewlab_get(request):
    data=Lab.objects.all()
    return render(request, "adminpage/view_lab.html",{'data':data})


def admin_viewlab_post(request):
    return


def admin_viewlabassist_get(request):
    return render(request, "adminpage/view_labassist.html")


def admin_viewlabassist_post(request):
    return


def admin_viewlabsub_get(request):
    data=Labsubject.objects.all()
    return render(request, "adminpage/view_labsub.html",{'data':data})


def admin_viewlabsub_post(request):
    return


def admin_viewlabsub_schedule_get(request):
    return render(request, "adminpage/view_labsub_schedule.html")


def admin_viewlabsub_schedule_post(request):
    return


def admin_viewstaff_get(request):
    return render(request, "adminpage/view_staff.html")


def admin_viewstaff_post(request):
    return


def admin_viewstudent_get(request):
    return render(request, "adminpage/view_student.html")


def admin_viewstudent_post(request):
    return


def admin_viewsystem_get(request):
    return render(request, "adminpage/view_system.html")


def admin_viewsystem_post(request):
    return


def admin_blockedapps_get(request):
    return render(request, "adminpage/blocked_apps.html")


def admin_blockedapps_post(request):
    return


def admin_viewattendance_report_get(request):
    return render(request, "adminpage/view_attendance_report.html")


def admin_viewstaff_suballoc_get(request):
    return render(request, "adminpage/view_staff_sub_allocation.html")





#ending of admin module








#lab assistant module

def labassist_addsys_healthreport_get(request):
    return render(request,"labassistpage/labassist_add_sys_health_rep.html")

def labassist_addsys_healthreport_post(request):
    return



def labassist_allocatesys_student_get(request):
    return render(request,"labassistpage/labassist_allocate_sys_student.html")

def labassist_allocatesys_student_post(request):
    return


def labassist_syst_monitor_get(request):
    return render(request,"labassistpage/labassist_system_monitor.html")

def labassist_syst_monitor_post(request):
    return


def labassist_view_alloc_lab_get(request):
    return render(request,"labassistpage/labassist_view_allocated_labs.html")

def labassist_view_profile_get(request):
    return render(request,"labassistpage/labassist_view_profile.html")

def labassist_view_sys_allocation_get(request):
    return render(request, "labassistpage/labassist_view_sys_allocation.html")


def labassist_view_sys_healthreport_get(request):
    return render(request, "labassistpage/labassist_view_sys_health_reports.html")

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
    return render(request,"staffpage/staff_view_profile.html")



def staff_view_system_get(request):
    return render(request,"staffpage/staff_view_system.html")


def staff_view_alloc_sub_get(request):
    return render(request,"staffpage/staff_view_allocated_subject.html")



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




