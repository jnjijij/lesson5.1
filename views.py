from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm

# List all cars
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

# Create a new car
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car_create.html', {'form': form})

# Update an existing car
def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'car_update.html', {'form': form})

# Delete a car
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'car_delete.html', {'car': car})
