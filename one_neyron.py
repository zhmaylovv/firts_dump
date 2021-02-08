class Neyron ():
    def __init__ (self):
        self.weight = 0.5
        self.error = 1
        self.smooth = 0.0001
        self.itter = 0

        #self.input = inputt
        #self.result = result
    def calc (self, input):
        return self.weight * input

    def restore (self, result):
        return result / self.weight

    def train (self, inputt, result):
        self.calculated_result = inputt * self.weight
        self.error = result - self.calculated_result
        correction = (self.error / self.calculated_result) * self.smooth
        self.weight += correction


km = 100
mile = 62.1371
neyron1 = Neyron()


while neyron1.error > 0.001:

    neyron1.train(km, mile)
    neyron1.itter += 1
    print('Попытка: ' + str(neyron1.itter) + "   Промежуточное значение: " + str(neyron1.calculated_result) + "Текущая ошибка:  " + str(neyron1.error))



print(neyron1.calc (input=km))
