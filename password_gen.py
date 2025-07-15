import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    chars = letters
    if use_digits:
        chars += digits
    if use_symbols:
        chars += symbols

    if not chars:
        raise ValueError("Нет доступных символов для генерации пароля.")

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔐 Генератор паролей")

    try:
        length = int(input("Введите длину пароля: "))
        use_digits = input("Включать цифры? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Включать спецсимволы? (y/n): ").strip().lower() == 'y'

        result = generate_password(length, use_digits, use_symbols)
        print(f"\n✅ Ваш сгенерированный пароль: {result}")
    except ValueError:
        print("Ошибка: длина должна быть числом.")
