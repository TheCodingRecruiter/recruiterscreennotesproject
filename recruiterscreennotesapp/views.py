from django.shortcuts import render

# Create your views here.


  
from django.shortcuts import render

# Create your views here.
# recruiterscreen



from .forms import RecruiterScreenForm
# from .models import RecruiterScreen

# Create your views here.


def recruiterscreen(request):

    title = 'Recruiter Screen Notes'
    form = RecruiterScreenForm()


    context = {
        'title' : title,
        'form' : form,


    }
    return render(request, "recruiterscreennotesapp/recruiternotes.html", context)