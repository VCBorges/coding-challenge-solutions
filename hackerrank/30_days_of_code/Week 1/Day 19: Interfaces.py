# fazer uma função que some os divisores de um numero 'n'
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        h = []
        for i in range(1, n + 1):
            if n % i == 0:
                h.append(i)
        return sum(h)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print('I implemented: ' + type(my_calculator).__bases__[0].__name__)
print(s)
