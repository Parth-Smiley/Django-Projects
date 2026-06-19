from django.shortcuts import render
from django.http import HttpResponse
from.forms import ReservationForm

# Create your views here.
def ReservationView(request):
    form = ReservationForm()
    if(request.method == 'POST'):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successful")
    return render(request,"index.html",{'form' : form})