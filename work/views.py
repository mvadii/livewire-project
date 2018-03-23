from django.shortcuts import render

from jobs.models import Job
# Create your views here.

def allwork(request):
    jobs = Job.objects
    return render(request, 'work/allwork.html', {'jobs':jobs})