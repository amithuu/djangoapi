from django.shortcuts import render
from .models import CourseList

# Create your views here.
def firstpage(request):
    cource = CourseList.objects.all()
    return render(request, 'buildapi/firstpage.html', {'course':cource})

