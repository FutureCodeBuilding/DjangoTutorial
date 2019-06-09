from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# Create your views here.
from django.http import HttpResponse
from .forms import UserForm
from .models import Person

def index(request):
    #return TemplateResponse(request, "polls/index.html")
    listOfstuff = ["Item1", "Item2", "Item3"]
    dictionary = {1:"One", 2:"Two"}
    form = UserForm(field_order=["name", "age"])
    data = {"title" : "All your titles are belong to us", "body" : "This is a ambush", "list": listOfstuff, "dict":dictionary, "form" : form}
    return render(request, "polls/index.html", context=data)
    #return TemplateResponse(request,  "polls/index.html", data)

def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        form = UserForm(request.POST)
        if form.is_valid():
            obj, created = Person.objects.get_or_create(name=name, age=age)
            createdText = ""
            ObjectsList = Person.objects.all()

            ListObj = []
            for obj in ObjectsList:
                ListObj.append(obj.name+ "," + str(obj.age))
            if created:
                createdText += "Object has succesfull added"
            data = {"title": "Hello there, general " + name, "body": "Your age is " + age + "\n" + createdText, "form" : form, "Objs": ListObj}
        else:
            data = {"title": "You, shall not pass! ", "body": "Go away, we aren't happy to see you", "form" : form}
    return render(request, "polls/index.html", context=data)


def about(request):
    return HttpResponse("<h2>About</h2>")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")

def products(request, productId = 42):
    category = request.GET.get("cat", "")
    return HttpResponse("<h2>Product №{0}, Category : {1}</h2>".format(productId, category))

def users(request):
    id = request.GET.get("id", "1")
    name = request.GET.get("name", "Alex")
    return HttpResponse("<h2>User</h2> <h3>Id : {0}, Name : {1}</h3>".format(id, name))
