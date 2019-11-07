# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”


class Car:
    def __init__(self, make, model, year, distance, fuel=70, odometer=0):
        self.make = make
        self.model = model
        self.year = year
        self.distance = distance
        self.fuel = fuel
        self.odometer = odometer

        print(f'{model} от {make} {year}г. Произвотства \n')

    #расстояни и количесто топлива
    def drive(self, distance, fuel):
        self._add_distance()
        self._sub_fuel()
        print(
            'Количество топлива в баке: ', self.fuel,
            'расстояние на которое хватит бензина: ',
              self.fuel * 10, 'пройденное расстояние: ',
              self.distance, 'можно еще пройти: ',
              self.fuel * 10 - self.distance, 'km',
              'оставшееся топливо: ',
              self.fuel-(self.distance/10)
              )
        #проверка топлива
        if fuel / distance < 0.1 or fuel == 0:
            print('Мужик, не хватает топлива! Заправся уже!!!')

        else:
            print('Поехали :)')

    #добавление пройденного пути к одометру
    def _add_distance(self):
        self.odometer += distance

    #вычитание топлива
    def _sub_fuel(self):
        self.fuel / distance * 100


make = input('Введите марку: ')
model = input('Введите модель: ')
year = int(input('Введите год: '))
distance = int(input('Введите растояние: '))
fuel = int(input('Введите количество топлива: '))

car = Car(make, model, year, distance, fuel)
car.drive(distance, fuel)