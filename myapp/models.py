from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Departement(models.Model):
    departementname=models.CharField(max_length=20)

class Course(models.Model):
    coursename=models.CharField(max_length=200)
    totelsem=models.CharField(max_length=200)
    DEP = models.ForeignKey(Departement,on_delete=models.CASCADE)

class Labassistant(models.Model):
    labassistantname = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    dob = models.DateField()
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    USER = models.OneToOneField(User, on_delete=models.CASCADE)

class Staff(models.Model):
    staffname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    dob = models.DateField()
    pincode=models.CharField(max_length=50)
    USER=models.OneToOneField(User,on_delete=models.CASCADE)
    DEP =  models.ForeignKey(Departement,on_delete=models.CASCADE,default='')

class Student(models.Model):
    studentname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    dob = models.DateField()
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    photo = models.CharField(max_length=500)
    sem = models.CharField(max_length=500)
    COURSE =  models.ForeignKey(Course,on_delete=models.CASCADE)
    USER =  models.OneToOneField(User,on_delete=models.CASCADE)



class Lab(models.Model):
    labname=models.CharField(max_length=50)
    labno=models.CharField(max_length=50)


class Labsubject(models.Model):
    subject=models.CharField(max_length=50)
    COURSE=models.ForeignKey(Course,on_delete=models.CASCADE)
    sem=models.CharField(max_length=50)


class Laballocation(models.Model):
    date=models.DateField()
    status=models.CharField(max_length=50)
    LAB =models.ForeignKey(Lab,on_delete=models.CASCADE)
    LABASSIST = models.ForeignKey(Labassistant,on_delete=models.CASCADE)

class Labsuballocation(models.Model):
    date=models.DateField()
    status=models.CharField(max_length=50)
    LABSUB =models.ForeignKey(Labsubject,on_delete=models.CASCADE)
    STAFF = models.ForeignKey(Staff,on_delete=models.CASCADE)


class Labsubjectschedule(models.Model):
    day=models.CharField(max_length=50)
    fromtime=models.CharField(max_length=50)
    totime=models.CharField(max_length=50)
    LABALLOCATION =models.ForeignKey(Laballocation,on_delete=models.CASCADE)
    LABSUB = models.ForeignKey(Labsubject,on_delete=models.CASCADE)




class System(models.Model):
    systemno=models.CharField(max_length=50)
    macaddress=models.CharField(max_length=50)
    LABASSIST = models.ForeignKey(Labassistant,on_delete=models.CASCADE)



class Complaint(models.Model):
    complaint=models.CharField(max_length=500)
    status=models.CharField(max_length=50)
    reply=models.CharField(max_length=500)
    date=models.DateField(default='2004-02-21')
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)


class Systemallocation(models.Model):
    date=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
    SYSTEM = models.ForeignKey(System, on_delete=models.CASCADE,default='')


class Helprequest(models.Model):
    date = models.CharField(max_length=50)
    time=models.CharField(max_length=50,default='')
    status = models.CharField(max_length=50)
    STUDENT = models.ForeignKey(Student,on_delete=models.CASCADE)
    SYSTEM = models.ForeignKey(System,on_delete=models.CASCADE,default='')


class Newapps(models.Model):
    status= models.CharField(max_length=50)
    appname=  models.CharField(max_length=50)
    SYSTEM =models.ForeignKey(System,on_delete=models.CASCADE)

class ProcessLogs(models.Model):
    date=models.DateField()
    time=models.TimeField()
    appname=  models.CharField(max_length=50)
    SYSTEM =models.ForeignKey(System,on_delete=models.CASCADE)


class Filelogs(models.Model):
    operation= models.CharField(max_length=50)
    time= models.CharField(max_length=50)
    date= models.CharField(max_length=50)
    filename= models.CharField(max_length=50)
    SYSTEM =models.ForeignKey(System,on_delete=models.CASCADE)


class Keylogs(models.Model):
    date = models.CharField(max_length=50)
    time= models.CharField(max_length=50)
    keys=models.CharField(max_length=500,default='')
    SYSTEM =models.ForeignKey(System,on_delete=models.CASCADE)


class Screenshots(models.Model):
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    filename=models.CharField(max_length=500,default='')
    status=models.CharField(max_length=10,default='')
    SYSTEM =models.ForeignKey(System,on_delete=models.CASCADE)


class Blockedapps(models.Model):
    appname=models.CharField(max_length=50)



class Healthreport(models.Model):
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    solvedstatus= models.CharField(max_length=50)
    problem= models.CharField(max_length=500)
    SYSTEM = models.ForeignKey(System, on_delete=models.CASCADE)



class Attendance(models.Model):
    date = models.CharField(max_length=50)
    time =models.CharField(max_length=50)
    status= models.CharField(max_length=50)
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    SYSTEM = models.ForeignKey(System, on_delete=models.CASCADE)


class Command(models.Model):
    date= models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    command=models.CharField(max_length=500)
    STAFF =models.ForeignKey(Staff,on_delete=models.CASCADE)

class Labrequest(models.Model):
    date= models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    LAB=models.ForeignKey(Lab,on_delete=models.CASCADE)
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)


