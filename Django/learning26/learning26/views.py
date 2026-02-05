from django.http import HttpResponse
from django.shortcuts import render

# specific urls
def test(requset):
    return HttpResponse("Hello")
def AboutUs(request):
    return render(request,"about.html")
def ContactUs(request):
    return render(request,"contactus.html")
def home(requset):
    return render(requset,"home.html")
def movie(request):
    return render(request,"movie.html")
def shows(request):
    return render(request,"shows.html")
def news(request):
    return render(request,"news.html") 
def recipe(request):
     ingredient= ["onion","chilly","tomato","garlic","coriander"]
     data = {"name":"maggie","time":15,"ingredient":ingredient} 
     return render(request,"recipe.html",data)  
     from django.shortcuts import render

def cricket(request):
    player1 = ["virat", "Mohammed Siraj", "Rajat Patidar", "Anuj Rawat","Faf du Plessis"]
    player2 = ["Jadeja", "Raina", "Ashwin", "Shami", "Iyer","msdhoni"]
    teams ={
            "team1Name": "Royal Challanger Banglore",
            "cap1": "Virat Kohli",
            "1player": player1 ,
            "rcbtrophy": 1,
        
           "team2Name": "Chennai Super Kings",
            "cap2": "MS Dhoni",
            "2player": player2 ,
            "csktrophy": 5
    }


    return render(request, "cricket.html", teams)
   