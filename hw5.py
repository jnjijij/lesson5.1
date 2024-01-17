class Car:
    def __init__(self, id, brand, year, seats, body_type, engine_volume):
        self.id = id
        self.brand = brand
        self.year = year
        self.seats = seats
        self.body_type = body_type
        self.engine_volume = engine_volume

class CarRepository:
    def __init__(self):
        self.cars = []

    def create(self, car):
        self.cars.append(car)

    def read_all(self):
        return [(car.id, car.brand, car.year, car.seats, car.body_type, car.engine_volume) for car in self.cars]

    def read_by_id(self, car_id):
        for car in self.cars:
            if car.id == car_id:
                return car
        return None

    def update(self, updated_car):
        for i, car in enumerate(self.cars):
            if car.id == updated_car.id:
                self.cars[i] = updated_car
                return True
        return False

    def delete(self, car_id):
        for i, car in enumerate(self.cars):
            if car.id == car_id:
                del self.cars[i]
                return True
        return False

# Создание репозитория машин
car_repo = CarRepository()

# Создание новых машин
car1 = Car(1, 'Toyota', 2019, 5, 'sedan', 2.0)
car2 = Car(2, 'BMW', 2020, 4, 'coupe', 3.0)
car3 = Car(3, 'Mercedes', 2018, 5, 'sedan', 2.5)
car4 = Car(4, 'Audi', 2021, 5, 'suv', 2.0)
car5 = Car(5, 'Honda', 2017, 5, 'sedan', 1.6)
car6 = Car(6, 'Ford', 2019, 5, 'hatchback', 1.0)
car7 = Car(7, 'Chevrolet', 2020, 7, 'suv', 3.6)
car8 = Car(8, 'Nissan', 2016, 5, 'sedan', 2.2)
car9 = Car(9, 'Volkswagen', 2021, 5, 'hatchback', 1.4)
car10 = Car(10, 'Hyundai', 2019, 5, 'sedan', 1.8)

# Добавление машин в репозиторий
car_repo.create(car1)
car_repo.create(car2)
car_repo.create(car3)
car_repo.create(car4)
car_repo.create(car5)
car_repo.create(car6)
car_repo.create(car7)
car_repo.create(car8)
car_repo.create(car9)
car_repo.create(car10)

# Получение всех машин
all_cars = car_repo.read_all()
print(all_cars)
# [(1, 'Toyota', 2019, 5, 'sedan', 2.0), (2, 'BMW', 2020, 4, 'coupe', 3.0), (3, 'Mercedes', 2018, 5, 'sedan', 2.5),
#  (4, 'Audi', 2021, 5, 'suv', 2.0), (5, 'Honda', 2017, 5, 'sedan', 1.6), (6, 'Ford', 2019, 5, 'hatchback', 1.0),
#  (7, 'Chevrolet', 2020, 7, 'suv', 3.6), (8, 'Nissan', 2016, 5, 'sedan', 2.2), (9, 'Volkswagen', 2021, 5, 'hatchback', 1.4),
#  (10, 'Hyundai', 2019, 5, 'sedan', 1.8)]

# Чтение машины по id
car = car_repo.read_by_id(1)
print(car)
# Car(id=1, brand='Toyota', year=2019, seats=5, body_type='sedan', engine_volume=2.0)