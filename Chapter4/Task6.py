class Furniture:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

        self.string = string = ''.join(str(list(self.kwargs)).strip('[').strip(']'))

    def getFurniture(self):
        print(f'Общая площадь {self.getSizeHouse()}, '
              f'Остальная площадь ', f'{self.getHouseArea()}, 'f'вся мебель: {self.string}', f'площадь мебели: {self.getFurnSize()}')

    def getFurnSize(self):
        furnituresize = self.kwargs['whichBed'] + \
                         self.kwargs['metersWardrobe'] +\
                         self.kwargs['metersTable']
        return float(furnituresize)

    def getSizeHouse(self):
        return self.kwargs['sizeHouse']

    def getHouseArea(self):
        otherHouseSize = self.getSizeHouse() - (self.kwargs['whichBed'] + \
                         self.kwargs['metersWardrobe'] +\
                         self.kwargs['metersTable'])
        return float(otherHouseSize)

f1 = Furniture(sizeHouse = 50, whichBed = 4,
               metersWardrobe = 2, metersTable = 1.5)
f1.getFurniture()