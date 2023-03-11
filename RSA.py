import random


class RSA:
    # def __init__(self):
    #
    #     # self.__gen_p_q()
    #     # self.__gen_N()
    #     # print('Число N = ', self.N)
    #     # self.e = self.gen_e()
    #     # self.d = self.gen_d()
    #     # print('d = ', self.d)
    #     #
    #     # # self.secret = secret  # secret  # int(input('Введите секрет (число): '))
    #     # # print('Секрет: ', self.secret)
    #     # # self.enc_message = self.enc(self.secret, self.e)
    #     # # print('Зашифрованное сообщение: ', self.enc_message)
    #     # # self.dec_message = self.dec(self.enc_message, self.d)
    #     # # print('Дешифрованное сообщение: ', self.dec_message)

    def __init__(self):
        self.e = None

    def launch_RSA(self, secret: int):
        
        self.__gen_p_q()
        self.__gen_N()
        #print('Число N = ', self.N)
        self.e = self.gen_e()
        self.d = self.gen_d()
        #print('d = ', self.d)
        self.secret = secret
        self.enc_message = self.enc(self.secret, self.e)
        self.dec_message = self.dec(self.enc_message, self.d)

        return self.dec_message

    # метод __gen_p_q(self): pass
    # Генерация простых p и q
    def __gen_p_q(self):
        self.p = self.gen_prime_number()  # 47 #числа генерить аглоритм Соловья-Штрассена
        self.q = self.gen_prime_number()  # 71
        # print('p: ', self.p)

    # print('q: ', self.q)

    def set_secret(self, secret: int):
        self.secret = secret

    def get_public_key_e(self):
        return self.e

    def get_N(self):
        return self.N

    def get_d(self):
        return self.d

    def get_secret(self):
        return self.secret

    def get_dec_message(self):
        return self.dec_message

    def get_enc_message(self):
        return self.enc_message

    def get_p_q(self):
        return self.p, self.q

    def get_dec_message(self):
        return self.dec_message

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
        random_value_index = random.randint(10, len(array_of_prime_values) - 1)

        return list(array_of_prime_values)[random_value_index]

    # Генерация N
    def __gen_N(self):
        self.N = self.p * self.q

    # def is_prime(self, n: int):
    #     for d in range(2, int(n ** 0.5) + 1):
    #         if n % d == 0:
    #             return False
    #     return True

    def symbol_Jacobi(self, q: int, p: int): #тест
        s = 0
        u = q
        v = p
        while True:
            r = u % v
            k = t = 0
            while r % 2 == 0:
                k += 1
                r //= 2
            t = r
            s = (s + k * (v * v - 1) / 8 + (t - 1) * (v - 1) / 4) % 2
            if t == 1:
                if s:
                    return -1
                else:
                    return 1
            if t < 3:
                break
            u = v
            v = t

    def Solovey_Shtrassen(self, n: int): #тест
        k = 1
        for i in range(k):
            random_number_a = random.randint(2, n - 1)
            if self.gcd(random_number_a, n) > 1:
                return False
            elif random_number_a ** ((n - 1) // 2) % n != self.symbol_Jacobi(random_number_a, n) % n:
                return False
            else:
                return True
        pass

    def gcd(self, a: int, b: int): # Алг Евклида тест
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    def gen_e(self):
        e = 3
        arr_e = []
        while True:  # self.Solovey_Shtrassen(e) self.is_prime(e)
            if self.Solovey_Shtrassen(e) \
                    and e < (self.p - 1) * (self.q - 1) \
                    and self.gcd(e, self.N) == 1:
                arr_e.append(e)
                # print(arr_e, '->>>>', len(arr_e))
                e += 1
            elif e > (self.p - 1) * (self.q - 1):
                break
            else:
                e += 1
        return arr_e[random.randint(0, len(arr_e))]

    # ax + by = gcd(a,b)
    def extended_gcd(self, a: int, b: int): #РАЕ тест
        if a == 0:
            return b, 0, 1
        else:
            div, x, y = self.extended_gcd(b % a, a)
        return div, y - (b // a) * x, x

    def inverse(self, value: int, module: int): #поиск обратного тест
        mod, x, y = self.extended_gcd(value, module)
        if mod == 1: return x
        return 0

    # d  = e^-1 mod N
    def gen_d(self):
        res_d = self.inverse(self.e, (self.p - 1) * (self.q - 1))
        if res_d < 0:
            res_d += (self.p - 1) * (self.q - 1)
            return res_d
        else:
            return res_d
        # return self.inverse(self.e, (self.p-1)*(self.q - 1))

    def enc(self, m: int, e: int):
        return m ** e % self.N

    def dec(self, c: int, d: int):
        return c ** d % self.N
    # Метод ... для генерации d

    # метод шифрования и дешифрования
    # сообщения m

# ДОБАВИТЬ ТЕСТЫ
# Генерация простых чисел (больших видимо) Алгоритм Соловья-Штрассена Решето Эратосфена
# Умножение по модулю алгоритм чтобы не выйти за инт
# rsa = RSA()
# # print(rsa.symbol_Jacobi(-104,997))
# print(rsa.extended_gcd(12,6))