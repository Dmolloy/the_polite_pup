from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Booking
from .forms import BookingForm


def home(request):
    return render(request, 'bookings/home.html')


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def create_booking(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})


@login_required
def edit_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)

    return render(
        request,
        'bookings/edit_booking.html',
        {'form': form}
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(user=request.user)

    return render(
        request,
        'bookings/my_bookings.html',
        {'bookings': bookings}
    )

@login_required
def delete_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')

    return render(
        request,
        'bookings/delete_booking.html',
        {'booking': booking}
    )