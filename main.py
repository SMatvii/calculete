import subprocess
import sys
import os
import webbrowser


def run_calculator(script_name):
    try:
        python_exe = "E:/calculete/.venv/Scripts/python.exe"
        subprocess.run([python_exe, script_name], check=True)
    except FileNotFoundError:
        print(f"Помилка: Файл {script_name} не знайдено!")
    except Exception as e:
        print(f"Помилка при запуску: {e}")


def open_html_file(html_file):
    try:
        file_path = os.path.abspath(html_file)
        webbrowser.open(f"file://{file_path}")
        print(f"HTML файл відкрито в браузері: {html_file}")
    except Exception as e:
        print(f"Помилка при відкритті HTML файлу: {e}")


def main():
    print("=" * 60)
    print("              КАЛЬКУЛЯТОРИ НА PYTHON")
    print("=" * 60)
    print()
    print("Виберіть тип калькулятора:")
    print("1. Повнофункціональний консольний калькулятор")
    print("2. Простий калькулятор (введення виразів)")  
    print("3. Графічний калькулятор (GUI)")
    print("4. HTML калькулятор з анімаціями (відкрити в браузері)")
    print("5. Простий HTML калькулятор (відкрити в браузері)")
    print("6. Головна HTML сторінка (відкрити в браузері)")
    print("7. Вихід")
    print()
    print("=" * 60)
    
    while True:
        try:
            choice = input("Ваш вибір (1-7): ").strip()
            
            if choice == '1':
                print("\nЗапускаємо повнофункціональний калькулятор...")
                run_calculator("templates\calculator.py")
                break
            
            elif choice == '2':
                print("\nЗапускаємо простий калькулятор...")
                run_calculator("main\simple_calculator.py")
                break
            
            elif choice == '3':
                print("\nЗапускаємо GUI калькулятор...")
                run_calculator("main\gui_calculator.py")
                break
            
            elif choice == '4':
                print("\nВідкриваємо HTML калькулятор в браузері...")
                open_html_file("templates\calculator.html")
                break
            
            elif choice == '5':
                print("\nВідкриваємо простий HTML калькулятор в браузері...")
                open_html_file("templates\simple_calculator.html")
                break
            
            elif choice == '6':
                print("\nВідкриваємо головну HTML сторінку в браузері...")
                open_html_file("templates\index.html")
                break
            
            elif choice == '7':
                print("До побачення!")
                break
            
            else:
                print("Невірний вибір! Будь ласка, введіть число від 1 до 7.")
        
        except KeyboardInterrupt:
            print("\n\nПрограму перервано. До побачення!")
            break
        except Exception as e:
            print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    main()
