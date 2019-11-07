class DollarFmt:
    def __init__(self, dollars):
        self.dollars = dollars

    def __str__(self):
        dollars2 = self.dollars
        dollars2 = round(self.dollars, 2)

        totalFloat = ''

        if type(dollars2) == float:
            dollars2 = str(dollars2)
            dollars2 = dollars2[::-1]

            for i in range(3):
                totalFloat += dollars2[i]

            totalFoalt = totalFloat[::-1]

        self.dollars = int(self.dollars)
        stringDollar = str(self.dollars)[::-1]
        listString = list(stringDollar)

        minus = False
        floatDollars = False

        if listString[-1] == '-':
            listString.pop(-1)
            minus = True
        if '.' in totalFloat:
            floatDollars = True

        for i in range(stringDollar.__len__()):
            if i % 4 == 0:
                listString.insert(i + 3, ',')

        listString = listString[::-1]
        if listString[0] == ',':
            listString.pop(0)

        if minus:
            listString.insert(0, '-')

        if floatDollars:
            listString.append(totalFloat[::-1])

        totalString = ''.join(listString)
        return totalString


dollarize = DollarFmt(123456.78)
print(dollarize)