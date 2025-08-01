def simple_calculator():
    print("ПРОСТИЙ КАЛЬКУЛЯТОР")
    print("Введіть математичний вираз (наприклад: 2 + 3, 10 / 2, 5 ** 2)")
    print("Для виходу введіть 'quit' або 'exit'")
    print("===========================")
    
    while True:
        try:
            expression = input("\nВведіть вираз: ").strip()
            
            if expression.lower() in ['quit', 'exit', 'вихід']:
                print("До побачення!")
                break
            
            allowed_chars = set('0123456789+-*/().** ')
            if not all(c in allowed_chars for c in expression):
                print("Помилка: Використовуйте тільки цифри та операції +, -, *, /, **, ()")
                continue
            
            result = eval(expression)
            print(f"Результат: {expression} = {result}")
            
        except ZeroDivisionError:
            print("Помилка: Ділення на нуль!")
        except ValueError:
            print("Помилка: Неправильний формат числа!")
        except SyntaxError:
            print("Помилка: Неправильний синтаксис виразу!")
        except Exception as e:
            print(f"Помилка: {e}")


if __name__ == "__main__":
    simple_calculator()
