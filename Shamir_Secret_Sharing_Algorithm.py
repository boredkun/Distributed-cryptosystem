# Класс
# Схемы 5 из 3 и тд просто больше точек
# 5 человек и любые 3 из них могут собрать
# в конструкторе определяем схему 5, 3 например
# Я могу обратиться к классу сказать свой номер мне отдадут значение
# Есть функция, которая позволяет собрать секрет - в нее передается массив где есть пары: (№ участника, значение) и она возвращает секрет
# деление по модулю (умножение на обратное)
import random


class ShamirSecretSharing:
    #names_of_users = []

    # def __init__(self, admin_or_user: bool, data: []):
    #     if admin_or_user:
    #         self.__set_admin(data[0], data[1], data[2])
    #         self.numbers_of_users = [i for i in range(1, data[1]+1)]
    #         #self.names_of_users = []
    #     else:
    #         self.__set_user(data[0])
    def __init__(self, k: int, n: int, secret: int):
        self.k = k
        self.n = n
        self.secret = secret
        self.module = self.gen_prime_number()
        #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!КОНСТРУКТОР!!!!!!')
        #print('Модуль: ', self.module)
        #print('n = ', self.n)
        #print('k = ', self.k)

        self.check()

    # составление секрета
    # из секрета составляю точку (0, secret)
    # составляем функцию степени k-1 со случайными коэфициентами по модулю
    # для этой функции вычисляем точки
    # Раздаем точки n - сторонам
    # Собираем точки с любых k сторон
    # проверяем секрет

    # def check_test(self):
    #     print(self.nodes)

    # def setUp(self):
    #     self.nodes = []
    #     for i in range(self.n):
    #         self.nodes.append((self.names_of_users[i], self.numbers_of_users))

    # def add_User(self, name: str):
    #     self.names_of_users.append(name)
    #
    # def __set_user(self, name: str):
    #     # self.number = random.randint(0, self.n) #?
    #     self.names_of_users.append(name)
    #
    # def __set_admin(self, k: int, n: int, secret: int):
    #     self.k = k
    #     self.n = n
    #     self.secret = secret
    #     self.module = self.gen_prime_number()

    # составляем функцию степени k-1 со случайными коэфициентами по модулю
    def gen_k_random_coefficients(self):
        arr = []
        arr.append(self.secret)
        for i in range(self.k - 1):
            arr.append(random.randint(1, 100000) % self.module)
       # print('Коэфициеты: ', arr)
        return arr

    def calculate_n_points(self):
        arr = []
        coefficients = self.gen_k_random_coefficients()
        arr_x_flag = []
        for i in range(self.n):
            value = 0
            x = random.randint(1, 100000) % self.module  # та же проблема в рса !"!!!!!!
            if x in arr_x_flag:
                while True:
                    x = random.randint(1, 100000) % self.module
                    if x not in arr_x_flag:
                        break
            arr_x_flag.append(x)
            for digit in range(1, self.k + 1):
                value += coefficients[digit - 1] * x ** (digit - 1)
            arr.append((x, value % self.module))
        #print('n - точек: ', arr)
        return arr

    def sharing(self, number: int):
        # dots = calculate_n_points()
        # Идея класс computers
        # люди по номерам получают свои точки
        pass

    def check(self):
        dots = self.calculate_n_points()
        arrX = []
        arrY = []
        for i in range(self.k):
            x, y = dots[i]
            arrX.append(x)
            arrY.append(y)
        dec_secret = self.lagranzh(arrX, arrY, self.module)
        #print(dec_secret)
        return dec_secret

    # решето эратосфена
    def gen_prime_number(self):
        random_value = random.randint(100, 500)
        # print(random_value)
        array_of_prime_values = [i for i in range(random_value + 1)]
        array_of_prime_values[1] = 0
        i = 2
        while i <= random_value:
            if array_of_prime_values[i] != 0:
                j = i + i
                while j <= random_value:
                    array_of_prime_values[j] = 0
                    j = j + i
            i += 1
        array_of_prime_values = set(array_of_prime_values)
        array_of_prime_values.remove(0)
        random_value_index = random.randint(10, len(array_of_prime_values) - 1)  # !!!!

        while list(array_of_prime_values)[random_value_index] <= self.secret:
            random_value_index = random.randint(10, len(array_of_prime_values) - 1)

        return list(array_of_prime_values)[random_value_index]

    def extended_gcd(self, a: int, b: int):  # РАЕ тест
        if a == 0:
            return b, 0, 1
        else:
            div, x, y = self.extended_gcd(b % a, a)
        return div, y - (b // a) * x, x

    def inverse(self, value: int, module: int):  # поиск обратного тест
        mod, x, y = self.extended_gcd(value, module)
        if mod == 1: return x
        return 0

    def lagranzh(self, x: [], y: [], module: int):
        z = 0
        for j in range(len(y)):
            p1 = 1
            p2 = 1
            for i in range(len(x)):
                if i == j:
                    p1 = (p1 * 1) % module
                    p2 = (p2 * 1) % module
                else:
                    p1 = (p1 * (0 - x[i])) % module
                    p2 = (p2 * (x[j] - x[i])) % module
            z = (z + y[j] * p1 * self.inverse(p2, module)) % module
        return z


# class Users:
#     def __init__(self, name: str):
#         self.number = 0
#         self.dot = (0, 0)
#         ShamirSecret = ShamirSecretSharing(False, [name])  # поменять в классе
#
#     def get_dot(self):
#         pass
#         # self.dot = ShamirSecret.get_dot(self.number)
#
#     def send_dot(self):
#         pass
        # ShamirSecret.send(self.number, self.dot())

# secret = 42
# ShamirSecret = ShamirSecretSharing(3, 5, secret)
# while ShamirSecret.check() == secret:
#     ShamirSecret.check()

