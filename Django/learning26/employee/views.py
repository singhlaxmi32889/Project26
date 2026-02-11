from django.shortcuts import render, HttpResponse
from .models import Employee,Course,Teacher,Productf,Studentf
from .froms import EmployeeForm,CourseForm,TeacherForm,ProductForm,StudentForm

# Create your views here.
def employeeList(request):
    #employees = Employee.objects.all() #select * from employee
    employees = Employee.objects.all().values()
    #employees = Employee.objects.all().values_list()
    print(employees)
    return render(request, 'employee/employeeList.html',{"employees":employees})

def employeeFilter(request):
    #where select  from employee where name = "Laxmi"
    employee = Employee.objects.filter(name ="Laxmi").values()
    #selet  from employee where post = "Developer"
    employee2 = Employee.objects.filter(post ="Developer").values()
    #select  from employee where name = "Laxmi" and post = "Developer"
    employee3 = Employee.objects.filter(name ="Laxmi",post ="Developer").values()
    #select  from employee where name = "Laxmi" or post = "Developer"

    #>23
    #seelct  from employee where age > 23
    #employee4 = Employee.objects.filter(age>23).values()
    employee4 = Employee.objects.filter(age__gt=23).values()
    employee5 = Employee.objects.filter(age__gte=23).values()

    #lt , lte

    #string queries
    employee6 = Employee.objects.filter(post__exact="Developer").values()
    employee7 = Employee.objects.filter(post__iexact="developer").values()
    #contains
    employee8 = Employee.objects.filter(name__contains="Laxmi").values()
    employee9 = Employee.objects.filter(name__icontains="Laxmi").values()

    #startswith endswith
    employee10 = Employee.objects.filter(name__startswith="Laxmi").values()
    employee11 = Employee.objects.filter(name__endswith="Laxmi").values()
    employee12 = Employee.objects.filter(name__istartswith="Laxmi").values()
    employee13 = Employee.objects.filter(name__iendswith="Laxmi").values()

    #in
    employee14 = Employee.objects.filter(name__in=["Laxmi","Mihir"]).values()    

    #range
    employee15 = Employee.objects.filter(age__range=[24,30]).values()    

    #order by
    employee16 = Employee.objects.order_by("age").values()     #asc
    employee17 = Employee.objects.order_by("-age").values()    #desc

    employee18 = Employee.objects.order_by("-salary").values()    #desc

    

    #and
    print("query 1",employee)
    print("query 2",employee2)
    print("query 3",employee3)
    print("query 4",employee4)
    print("query 5",employee5)
    print("query 6",employee6)   
    print("query 7",employee7) 
    print("query 8",employee8) 
    print("query 9",employee9) 
    print("query 10",employee10) 
    print("query 11",employee11) 
    print("query 12",employee12) 
    print("query 13",employee13) 
    print("query 14",employee14) 
    print("query 15",employee15) 
    print("query 16",employee16) 
    print("query 17",employee17) 
    return render(request, 'employee/employeeFilter.html')

def createEmployeeWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save() #it same as create
        return HttpResponse("EMPLOYEE CREATED...")
    else:
        #form object create --> html
        form = EmployeeForm() #form object        
        return render(request,"employee/createEmployeeForm.html",{"form":form})

def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST) #csrftoken,form alll fileds data
        form.save() #create.. insert into table 
        return HttpResponse("COURSE CREATED...")
    else:
        form = CourseForm()
        return render(request,"employee/createCourse.html",{"form":form})

def createTeacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST) #csrftoken,form alll fileds data
        form.save() #create.. insert into table 
        return HttpResponse("TEACHER CREATED...")
    else:
        form = TeacherForm()
        return render(request,"employee/createTeacher.html",{"form":form})    

def createProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST) #csrftoken,form alll fileds data
        form.save() #create.. insert into table 
        return HttpResponse("PRODUCT CREATED...")
    else:
        form = ProductForm()
        return render(request,"employee/createProduct.html",{"form":form})    

def createStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST) #csrftoken,form alll fileds data
        form.save() #create.. insert into table 
        return HttpResponse("STUDENT CREATED...")
    else:
        form = StudentForm()
        return render(request,"employee/createStudent.html",{"form":form})    

