

class Airplane:
    def __init__(self, make, model, year, max_speed, fly_range, odometer=0, is_flying=False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.fly_range = fly_range
        self.odometer = odometer
        self.is_flying = is_flying


    def turn_off(self):
        # a = partial(bool, is_flying = True)
        self.is_flying = True

    def land(self):
        # a = partial(bool, is_flying = False)
        self.is_flying = False

    def fly(self):
        self.odometer += fly_range

    def all_info(self):
        return f"{self.make}--{self.model}--{self.year}--" \
               f"{self.max_speed}--{self.fly_range}"


make = input('Марка самолета: ')
model = input('Модель самолета: ')
year = int(input('Начало эксплуатации: '))
max_speed = int(input('Скорость полета: '))
fly_range = int(input('Расстояние полета: '))


airplane = Airplane(make, model, year, max_speed, fly_range)
print(airplane.all_info())
airplane.turn_off()
print(airplane.is_flying)
airplane.fly()
print('Пройденное расстояние =', airplane.odometer)
airplane.land()
print(airplane.is_flying)
