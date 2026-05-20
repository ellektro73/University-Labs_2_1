def calculate_z(x, y):
    if x > 8:
        z = 3 + y
        print(f"Обчислення за умовою x > 8: z = 3 + {y}")
    else:
        z = 9 * x * y
        print(f"Обчислення за умовою x <= 8: z = 9 * {x} * {y}")
    return z


def calculate_factorial(n):
    if n < 0:
        return "Факторіал не існує для від'ємних чисел"

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    print("Завдання 1: Обчислення виразу z ")
    try:
        user_x = float(input("Введіть x: "))
        user_y = float(input("Введіть y: "))

        z_result = calculate_z(user_x, user_y)
        print(f"Результат z = {z_result}")

        print("\nЗавдання 2: Обчислення факторіала n!")
        user_n = int(input("Введіть ціле число n: "))

        fact_result = calculate_factorial(user_n)
        print(f"Результат {user_n}! = {fact_result}")

    except ValueError:
        print("Помилка: будь ласка, вводьте лише числові значення.")


if __name__ == "__main__":
    main()