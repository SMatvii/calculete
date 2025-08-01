import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return
    return x / y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Помилка: Не можна взяти корінь з від'ємного числа!"
    return math.sqrt(x)


def display_menu():
    print("\n=== КАЛЬКУЛЯТОР ===")
    print("Виберіть операцію:")
    print("1. Додавання (+)")
    print("2. Віднімання (-)")
    print("3. Множення (*)")
    print("4. Ділення (/)")
    print("5. Піднесення до степеня (**)")
    print("6. Квадратний корінь (√)")
    print("7. Вихід")
    print("==================")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: Введіть дійсне число!")


def main():
    print("Ласкаво просимо до простого калькулятора!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Ваш вибір (1-7): ")
            
            if choice == '7':
                print("Дякуємо за використання калькулятора! До побачення!")
                break
            
            if choice in ['1', '2', '3', '4', '5']:
                num1 = get_number("Введіть перше число: ")
                num2 = get_number("Введіть друге число: ")
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"Результат: {num1} + {num2} = {result}")
                
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"Результат: {num1} - {num2} = {result}")
                
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"Результат: {num1} * {num2} = {result}")
                
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Результат: {num1} / {num2} = {result}")
                
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"Результат: {num1} ** {num2} = {result}")
            
            elif choice == '6':
                num = get_number("Введіть число для обчислення квадратного кореня: ")
                result = square_root(num)
                print(f"Результат: √{num} = {result}")
            
            else:
                print("Невірний вибір! Будь ласка, виберіть число від 1 до 7.")
        
        except KeyboardInterrupt:
            print("\n\nПрограму перервано користувачем. До побачення!")
            break
        except Exception as e:
            print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    main()
