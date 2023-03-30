import time
import os


class Calculator:
    def __init__(self, *args):
        self.args = args
        
    def add(self):
        total = 0
        for num in self.args:
            total += num
        return total
    
    def subtract(self):
        total = self.args[0]
        for num in self.args[1:]:
            total -= num
        return total
    
    def divide(self):
        total = self.args[0]
        for num in self.args[1:]:
            total /= num
        return total
    
    def multiply(self):
        total = self.args[0]
        for num in self.args[1:]:
            total *= num
        return total


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Wybierz rodzaj wykonywanego polecenia: ")
    print("1: Dodawanie")
    print("2: Odejmowanie")
    print("3: Mnożenie")
    print("4: Dzielenie")
    print("5: Zakończ")
    time.sleep(0.5)
    choice = input("Wybierz opcję: ")
    print("The program is loading...")
    
    
    time.sleep(5)
    print("[=====               ] 25%")
    time.sleep(5)
    print("[==========          ] 50%")
    time.sleep(5)
    print("[===============     ] 75%")
    time.sleep(5)
    print("[====================] 100%")
    time.sleep(2)
    
    if choice == "1":
        nums = list(map(int, input("Podaj liczby oddzielone przecinkiem: ").split(",")))
        calculator = Calculator(*nums)
        result = calculator.add()
        print("Wynik: ", result)
        time.sleep(2)
    elif choice == "2":
        nums = list(map(int, input("Podaj liczby oddzielone przecinkiem: ").split(",")))
        calculator = Calculator(*nums)
        result = calculator.subtract()
        print("Wynik: ", result)
        time.sleep(2)
    elif choice == "3":
        nums = list(map(int, input("Podaj liczby oddzielone przecinkiem: ").split(",")))
        calculator = Calculator(*nums)
        result = calculator.multiply()
        print("Wynik: ", result)
        time.sleep(2)
    elif choice == "4":
        nums = list(map(int, input("Podaj liczby oddzielone przecinkiem: ").split(",")))
        calculator = Calculator(*nums)
        result = calculator.divide()
        print("Wynik: ", result)
        time.sleep(2)
    elif choice == "5" or choice.lower() == "exit":
        break
    else:
        print("Nieprawidłowa opcja, spróbuj ponownie.")
        time.sleep(2)

print("Zamykanie programu...")
