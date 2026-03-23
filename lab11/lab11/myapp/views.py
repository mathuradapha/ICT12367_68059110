from django.shortcuts import render, redirect, get_object_or_404
from .models import Person


def home(request):
    data = Person.objects.all()
    return render(request,'index.html',{'data':data})


def form(request):

    if request.method == "POST":

        citizen_id = request.POST.get('citizen_id')
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        age = request.POST.get('age')

        Person.objects.create(
            citizen_id=citizen_id,
            name=name,
            nickname=nickname,
            age=age
        )

        return redirect('/')

    return render(request,'form.html')


def delete(request,id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect('/')


def edit(request,id):

    person = get_object_or_404(Person,id=id)

    if request.method == "POST":

        person.citizen_id = request.POST.get('citizen_id')
        person.name = request.POST.get('name')
        person.nickname = request.POST.get('nickname')
        person.age = request.POST.get('age')

        person.save()

        return redirect('/')

    return render(request,'edit.html',{'person':person})