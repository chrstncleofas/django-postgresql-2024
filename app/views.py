from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'app/base.html')

def list(request):
    return render(request, 'app/list.html', {
        'reservation' : Reservation.objects.all(),
    })

def list_item(request, id):
    reservations = Reservation.objects.get(pk=id)
    return HttpResponseRedirect(reverse('list'))

def add(request):
    if request.method == 'POST':
        new_fname = request.POST.get('fname')
        new_lname = request.POST.get('lname')
        new_address = request.POST.get('address')
        new_city = request.POST.get('city')
        new_province = request.POST.get('province')
        new_postal = request.POST.get('postal')
        new_email = request.POST.get('email')
        new_phone = request.POST.get('phone')
        arrival_date = request.POST.get('arrival_date')
        arrival_time = request.POST.get('arrival_time')
        departure_date = request.POST.get('departure_date')
        departure_time = request.POST.get('departure_time')
        number_person = request.POST.get('number_person')
        message = request.POST.get('message')

        reservation = Reservation.objects.create()

        reservation.fname = new_fname
        reservation.lname = new_lname
        reservation.address = new_address
        reservation.city = new_city
        reservation.province = new_province
        reservation.postal = new_postal
        reservation.email = new_email
        reservation.phone = new_phone
        reservation.arrival_date = arrival_date
        reservation.arrival_time = arrival_time
        reservation.departure_date = departure_date
        reservation.departure_time = departure_time
        reservation.number_person = number_person
        reservation.message = message

        reservation.save()

        return render(request, 'app/add.html',{
            'form': Reservation(),
            'success': True
        })
    else:
        return render(request, 'app/add.html',{
            'form': Reservation(),
        })
    
def edit_list(request, id):
    if request.method == 'POST':
        reservation = Reservation.objects.get(pk=id)
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return render(request, 'app/edit.html', {
                'form': form,
                'success': True,
            })
    else:
        reservation = Reservation.objects.get(pk=id)
        form = ReservationForm(instance=reservation)
    return render(request, 'app/edit.html',{
        'form': form,
    })


def delete_list(request, id):
    if request.method == 'POST':
        reservation = Reservation.objects.get(pk=id)
        reservation.delete()
    return HttpResponseRedirect(reverse('list'))
