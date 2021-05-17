from django.shortcuts import render
from django.http  import HttpResponse, HttpResponseRedirect
from os41.models import Student, Track
from os41.forms import studentForm, TrackForm
# Create your views here.
def home(request):
    return HttpResponse("<h1>hiiii</h1>")

def getstd (request,st_id):
    st = Student.objects.get(id= st_id)
    context = {'students' : st}
    return render(request,'os41/details.html',context)

    # return HttpResponse(st.fname)
def getallstds (request):
    allstds = Student.objects.all()
    context = {'students' : allstds}
    return render(request,'../templates/os41/students.html',context)

def newstd (request):
    std_form = studentForm()
    if request.method == 'POST':
        std_form = studentForm(request.POST)
        if std_form.is_valid():
            std_form.save()
            return HttpResponseRedirect('/os41/all')
    context = {'std_form': std_form}
    return render (request,'os41/new_student.html',context)

def editstudent (request,st_id):
    st = Student.objects.get(id = st_id)
    st_form = studentForm(instance=st)
    # de data mn object student ana 3mltlo create
    if request.method == 'POST' : #y3ny 7sl submit
        st_form = studentForm(request.POST, instance=st)
        if st_form.is_valid():
            st_form.save()
            return HttpResponseRedirect('/os41/all')

    context = {'std_form': st_form}
    return render (request,'os41/new_student.html',context)

def delstd (request, st_id):
    st = Student.objects.get(id = st_id)
    st.delete()
    return HttpResponseRedirect('/os41/all')
