# myapp/models.py
from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=100)
    engine_volume = models.FloatField()

    def __str__(self):
        return self.brand

# myapp/views.py
from django.shortcuts import render
from myapp.models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'myapp/car_list.html', {'cars': cars})

# myapp/templates/myapp/car_list.html
<!DOCTYPE html>
<html>
<head>
    <title>Car List</title>
</head>
<body>
    <h1>Car List</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Brand</th>
                <th>Year</th>
                <th>Seats</th>
                <th>Body Type</th>
                <th>Engine Volume</th>
            </tr>
        </thead>
        <tbody>
            {% for car in cars %}
            <tr>
                <td>{{ car.id }}</td>
                <td>{{ car.brand }}</td>
                <td>{{ car.year }}</td>
                <td>{{ car.seats }}</td>
                <td>{{ car.body_type }}</td>
                <td>{{ car.engine_volume }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
