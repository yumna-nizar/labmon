
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('login_get/',views.login_get),
    path('login_post/',views.login_post),

    path('admin_home/',views.admin_home),

    path('admin_changepassword_get/',views.admin_changepassword_get),
    path('admin_changepassword_post/',views.admin_changepassword_post),


    path('admin_addcourse_get/',views.admin_addcourse_get),
    path('admin_add_course_post/',views.admin_add_course_post),


    path('admin_add_department_get/',views.admin_add_department_get),
    path('admin_add_department_post/',views.admin_add_department_post),


    path('admin_addlab_get/',views.admin_addlab_get),
    path('admin_addlab_post/',views.admin_addlab_post),


    path('admin_addlabassist_get/',views.admin_addlabassist_get),
    path('admin_addlabassist_post/',views.admin_addlabassist_post),


    path('admin_addlabsub_get/',views.admin_addlabsub_get),
    path('admin_addlabsub_post/',views.admin_addlabsub_post),

    path('admin_addlabsub_schedule_get/',views.admin_addlabsub_schedule_get),

    path('admin_addlabsub_schedule_post/',views.admin_addlabsub_schedule_post),


    path('admin_addstaff_get/',views.admin_addstaff_get),
    path('admin_addstaff_post/',views.admin_addstaff_post),


    path('admin_addstudent_get/',views.admin_addstudent_get),
    path('admin_addstudent_post/',views.admin_addstudent_post),

    path('admin_addsystem_get/',views.admin_addsystem_get),
    path('admin_addsystem_post/',views.admin_addsystem_post),


    path('admin_assistallocation_get/',views.admin_assistallocation_get),
    path('admin_assistallocation_post/',views.admin_assistallocation_post),


    path('admin_editassistallocation_get/<id>',views.admin_editassistallocation_get),
    path('admin_deleteassistallocation_post/<id>',views.admin_deleteassistallocation_post),
    path('admin_editassistallocation_post/',views.admin_editassistallocation_post),

    path('admin_editcourse_get/<id>',views.admin_editcourse_get),
    path('admin_delete_course/<id>',views.admin_delete_course),
    path('admin_editcourse_post/',views.admin_editcourse_post),

    path('admin_editdepartment_get/<id>',views.admin_editdepartment_get),
    path('admin_delete_department/<id>',views.admin_delete_department),
    path('admin_editdepartment_post/',views.admin_editdepartment_post),


    path('admin_editlab_get/<id>',views.admin_editlab_get),
    path('admin_deletelab/<id>',views.admin_deletelab),
    path('admin_editlab_post/',views.admin_editlab_post),


    path('admin_editlabassist_get/<id>',views.admin_editlabassist_get),
    path('admin_deletelabassist_get/<id>',views.admin_deletelabassist_get),
    path('admin_editlabassist_post/',views.admin_editlabassist_post),


    path('admin_editlabsub_get/<id>',views.admin_editlabsub_get),
    path('admin_delete_labsub/<id>',views.admin_delete_labsub),
    path('admin_editlabsub_post/',views.admin_editlabsub_post),


    path('admin_editlab_schedule_get/<id>',views.admin_editlab_schedule_get),
    path('admin_deletelabsub_schedule_get/<id>',views.admin_deletelabsub_schedule_get),
    path('admin_editlab_schedule_post/',views.admin_editlab_schedule_post),

    path('admin_editstaff_get/<id>',views.admin_editstaff_get),
    path('admin_deletestaff_get/<id>',views.admin_deletestaff_get),
    path('admin_editstaff_post/',views.admin_editstaff_post),


    path('admin_editstudent_get/<id>',views.admin_editstudent_get),
    path('admin_deletestudent_get/<id>',views.admin_deletestudent_get),
    path('admin_editstudent_post/',views.admin_editstudent_post),


    path('admin_editsystem_get/',views.admin_editsystem_get),
    path('admin_editsystem_post/',views.admin_editsystem_post),


    path('admin_viewcourse_get/',views.admin_viewcourse_get),
    path('admin_viewcourse_post/',views.admin_viewcourse_post),


    path('admin_viewdepartment_get/',views.admin_viewdepartment_get),
    path('admin_viewdepartment_post/',views.admin_viewdepartment_post),


    path('admin_viewlab_get/',views.admin_viewlab_get),
    path('admin_viewlab_post/',views.admin_viewlab_post),


    path('admin_viewlabassist_get/',views.admin_viewlabassist_get),
    path('admin_viewlabassist_post/',views.admin_viewlabassist_post),



    path('admin_viewlabsub_get/',views.admin_viewlabsub_get),
    path('admin_viewlabsub_post/',views.admin_viewlabsub_post),


    path('admin_viewlabsub_schedule_get/',views.admin_viewlabsub_schedule_get),
    path('admin_viewlabsub_schedule_post/',views.admin_viewlabsub_schedule_post),


    path('admin_viewstaff_get/',views.admin_viewstaff_get),
    path('admin_viewstaff_post/',views.admin_viewstaff_post),


    path('admin_viewstudent_get/',views.admin_viewstudent_get),
    path('admin_viewstudent_post/',views.admin_viewstudent_post),

    path('admin_viewassist_allocation_get/',views.admin_viewassist_allocation_get),
    # path('admin_viewassist_allocation_post/',views.admin_viewassist_allocation_post),



    path('admin_viewsystem_get/',views.admin_viewsystem_get),
    # path('admin_viewsystem_post/',views.admin_viewsystem_post),


    path('admin_blockedapps_get/',views.admin_blockedapps_get),
    path('admin_blockedapps_post/',views.admin_blockedapps_post),


    path('admin_viewattendance_report_get/',views.admin_viewattendance_report_get),

    path('admin_staffsuballoc_get/',views.admin_staffsuballoc_get),
    path('admin_staffsuballoc_post/',views.admin_staffsuballoc_post),

    path('admin_edit_staffsuballoc_get/<id>',views.admin_edit_staffsuballoc_get),
    path('admin_edit_staffsuballoc_post/',views.admin_edit_staffsuballoc_post),
    path('admin_delete_staffsuballoc/<id>',views.admin_delete_staffsuballoc),

    path('admin_viewsuballoc/',views.admin_viewsuballoc),




    #starting of lab assistant module

    path('labassist_index_get/', views.labassist_index_get),




    path('admin_addsystem_get/', views.admin_addsystem_get),
    path('admin_addsystem_post/', views.admin_addsystem_post),
    path('admin_editsystem_get/<id>', views.admin_editsystem_get),
    path('admin_editsystem_post/', views.admin_editsystem_post),
    path('admin_deletesystem_get/<id>', views.admin_deletesystem_get),
    path('admin_viewsystem_get/', views.admin_viewsystem_get),

    path('labassist_addsys_healthreport_get/',views.labassist_addsys_healthreport_get),
    path('labassist_addsys_healthreport_post/',views.labassist_addsys_healthreport_post),


    path('labassist_allocatesys_student_get/',views.labassist_allocatesys_student_get),
    path('labassist_allocatesys_student_post/',views.labassist_allocatesys_student_post),


    path('labassist_syst_monitor_get/',views.labassist_syst_monitor_get),
    path('labassist_syst_monitor_post/',views.labassist_syst_monitor_post),


    path('labassist_view_alloc_lab_get/',views.labassist_view_alloc_lab_get),
    path('labassist_view_profile_get/',views.labassist_view_profile_get),


    path('labassist_view_sys_allocation_get/',views.labassist_view_sys_allocation_get),


    path('labassist_view_sys_healthreport_get',views.labassist_view_sys_healthreport_get),




#staff module

    path('staff_command_invoc_get/',views.staff_command_invoc_get),
    path('staff_command_invoc_post/',views.staff_command_invoc_post),


    path('staff_helpreq_get/',views.staff_helpreq_get),
    path('staff_helpreq_post/',views.staff_helpreq_post),


    path('staff_sentreply_get/',views.staff_sentreply_get),
    path('staff_sentreply_post/',views.staff_sentreply_post),


    path('staff_systmonitor_get/',views.staff_systmonitor_get),
    path('staff_systmonitor_post/',views.staff_systmonitor_post),


    path('staff_viewstud_complaint_get/',views.staff_viewstud_complaint_get),

    path('staff_view_profile_get/',views.staff_view_profile_get),

    path('staff_view_system_get/',views.staff_view_system_get),

    path('staff_view_alloc_sub_get/',views.staff_view_alloc_sub_get),

    path('staff_view_filelogs_get/',views.staff_view_filelogs_get),

    path('staff_view_keylogs_get/',views.staff_view_keylogs_get),

    path('staff_view_processlogs_get/',views.staff_view_processlogs_get),

    path('staff_view_scrnshot_get/',views.staff_view_scrnshot_get),













]
