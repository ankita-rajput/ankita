from django.shortcuts import render,HttpResponse,redirect
from firstapp.forms import SiteUserForm,UserRoleForm,ImageForm
from firstapp.models import SiteUser,UserRole,Image
from django.core.files.storage import FileSystemStorage    #to store image in ,edia directory in project--
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to  first response</h1>")
def home(request):
    return render(request,"home.html")
def about(request):
    name="Ankita"
    names=["ankit","vipin","arun"]
    return render(request,'about.html',{'n':name,'l':names})
def content1(request):
    return render(request,"content1.html")
def content2(request):
    return render(request,"content2.html")
def signup(request):
    if request.method=="POST":
        form=SiteUserForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.userFullName=request.POST["username"]
            f.userEmail=request.POST["useremail"]
            f.userPassword=make_password(request.POST["userpassword"])
            f.userMobile=int(request.POST["usermobile"])
            f.isActive=1
            f.roleId_id=2
            f.save()
        else:
            return HttpResponse("not valid")
        return render(request,"signup.html",{'success':True})
    return render(request, "signup.html")


def login(request):
    if request.method=="POST":
        form = UserRoleForm(request.POST)
        if form.is_valid():
            f= form.save(commit=False)
            f.roleName=request.POST["rolename"]
            f.isActive=True
            f.save()
            return render(request, "login.html",{'success':True})

    return render(request,"login.html")


#get(),filter(),all()
def viewdata(request):
    data=SiteUser.objects.all()
    # data=SiteUser.objects.filter(isActive=1)
    return render(request,"viewdata.html",{'d':data})

def fetchingonevalue(request):
    data = SiteUser.objects.get(userEmail="shivam00347@gmail.com")
    return render(request,"fetchingonevalue.html",{'d':data})

def imageform(request):
    if request.method=="POST":
        form = ImageForm(request.POST)
        img = None
        try:
            if request.FILES["userimage"]:
                my_file = request.FILES["userimage"]
                fs=FileSystemStorage()   #used to store images in database---
                file_name= fs.save(my_file.name,my_file)
                img= fs.url(file_name)
                img = my_file
        except:
            pass
        f = form.save(commit=False)
        f.userFullName = request.POST["username"]
        f.userEmail = request.POST["useremail"]
        f.userPassword = make_password(request.POST["userpassword"])
        f.userMobile = int(request.POST["usermobile"])
        f.userImage = img
        f.isActive = 1
        f.roleId_id = 2
        f.save()
        return render(request, "imageform.html", {'success': True})
    return render(request,"imageform.html")

def updateform(request):
    if request.method == "POST":
        emailid = request.POST["useremail"]
        npassword = make_password(request.POST["userpassword"])
        mobile = request.POST["usermobile"]
        updatedata=SiteUser(userEmail=emailid,userPassword=npassword,userMobile=mobile)
        updatedata.save(update_fields=["userPassword","userMobile"])
        return render(request, "updateform.html", {'success': True})
    return render(request, "updateform.html")

def deletedata(request):
    emailid = request.GET["id"]
    data = SiteUser.objects.get(userEmail=emailid)
    data.delete()
    return redirect("/user/viewdata/")
def action(request):
    emailid = request.GET["id"]
    data = Image.objects.get(userEmail=emailid)
    if request.method == "POST":
        npassword = make_password(request.POST["userpassword"])
        mobile = request.POST["usermobile"]
        updatedata=SiteUser(userEmail=emailid,userPassword=npassword,userMobile=mobile)
        updatedata.save(update_fields=["userPassword", "userMobile"])
        return redirect("/user/viewdata")
    return render(request,"updatedata.html",{'a':data})

def imageviewdata(request):
    data=Image.objects.all()
    return render(request,"imageviewdata.html",{'b':data})

def deleteimageformdata(request):
    emailid = request.GET["id"]
    data = Image.objects.get(userEmail=emailid)
    data.delete()
    return redirect("/user/imageviewdata/")

def imageupdate(request):
    emailid = request.GET["id"]
    data = Image.objects.get(userEmail=emailid)
    if request.method == "POST":
        userimage = request.FILES.get('userimage')  # Use request.FILES
        form = ImageForm(request.POST)
        img = userimage
        try:
            if request.FILES["userimage"]:
                my_file = request.FILES["userimage"]
                fs=FileSystemStorage()   #used to store images in database---
                file_name= fs.save(my_file.name,my_file)
                img= fs.url(file_name)
                img = my_file
        except:
            pass

        name = request.POST["username"]
        npassword = make_password(request.POST["userpassword"])
        mobile = request.POST["usermobile"]
        userimage=img
        updatedata = Image(userEmail=emailid,userFullName=name,userPassword=npassword, userMobile=mobile,userImage=userimage)
        updatedata.save(update_fields=["userFullName","userPassword", "userMobile","userImage"])
        return redirect("/user/imageviewdata")
    return render(request, "imageupdateform.html", {'b': data})

