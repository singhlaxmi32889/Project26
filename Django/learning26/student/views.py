from django.shortcuts import render

# Create your views here.
def studenthome(request):
    return render(request,"student/studenthome.html")
def studentlist(request):
    name=["laxmi","ruhi","aayu","sid","parth"]
    age=[20,23,25,18,22]
    city=["ahmedabad","delhi","mumbai","kanpur","gorakhpur"]
    student={"name":name,"city":city,"age":age}

    return render(request,"student/studentlist.html",{"student":student})
