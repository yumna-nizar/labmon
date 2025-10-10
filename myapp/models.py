from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Departement(models.Model):
    departementname=models.CharField(max_length=20)

class Course(models.Model):
    coursename=models.CharField(max_length=20)
    totelsem=models.CharField(max_length=20)
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
    COURSE =  models.ForeignKey(Course,on_delete=models.CASCADE)



class Lab(models.Model):
    labname=models.CharField(max_length=20)
    labno=models.CharField(max_length=20)


class Labsubject(models.Model):
    subject=models.CharField(max_length=20)

class Laballocation(models.Model):
    date=models.DateField()
    status=models.CharField(max_length=20)
    LAB =models.ForeignKey(Lab,on_delete=models.CASCADE)
    LABASSIST = models.ForeignKey(Labassistant,on_delete=models.CASCADE)

class Labsuballocation(models.Model):
    date=models.DateField()
    status=models.CharField(max_length=20)
    LABSUB =models.ForeignKey(Labsubject,on_delete=models.CASCADE)
    STAFF = models.ForeignKey(Staff,on_delete=models.CASCADE)


class Labsubjectschedule(models.Model):
    day=models.CharField(max_length=20)
    fromtime=models.CharField(max_length=20)
    totime=models.CharField(max_length=20)
    LABALLOCATION =models.ForeignKey(Laballocation,on_delete=models.CASCADE)
    LABSUB = models.ForeignKey(Labsubject,on_delete=models.CASCADE)




class System(models.Model):
    systemno=models.CharField(max_length=20)
    macaddress=models.CharField(max_length=20)
    LAB=models.ForeignKey(Lab,on_delete=models.CASCADE,default='')



class Complaint(models.Model):
    complaint=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    reply=models.CharField(max_length=20)


class Systemallocation(models.Model):
    date=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
    SYSTEM = models.ForeignKey(System, on_delete=models.CASCADE,default='')


class Helprequest(models.Model):
    date = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    STUDENT = models.ForeignKey(Student,on_delete=models.CASCADE)
    STAFF =models.ForeignKey(Staff,on_delete=models.CASCADE)


class Newapps(models.Model):
    status= models.CharField(max_length=50)
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
    SYSTEM =models.ForeignKey(System,on_delete=models.CASCADE)


class Screenshots(models.Model):
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    SYSTEM =models.ForeignKey(System,on_delete=models.CASCADE)


class Blockedapps(models.Model):
    appname=models.CharField(max_length=50)



class Healthreport(models.Model):
    solvedstatus= models.CharField(max_length=50)
    problem= models.CharField(max_length=50)
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
    STAFF =models.ForeignKey(Staff,on_delete=models.CASCADE)


class Attendace(models.Model):
      date=models.CharField(max_length=50)
      STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
      status = models.CharField(max_length=50)
















