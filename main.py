import unittest
from RSA import RSA
from Shamir_Secret_Sharing_Algorithm import ShamirSecretSharing
import random

''' -------------Tests----------------'''


class TestRSA(unittest.TestCase):

    def setUp(self):
        self.rsa = RSA()
        self.shamir1 = ShamirSecretSharing(5, 10, 43)


    def test_work_RSA_1(self):
        self.assertEqual(self.rsa.launch_RSA(secret=40), 40)
        print('N = ', self.rsa.get_N(), '\np,q = ', self.rsa.get_p_q(),
              '\npublic key e = ', self.rsa.get_public_key_e(), '\nprivate key d: ', self.rsa.get_d(),
              '\nsecret: ', self.rsa.get_secret(),
              '\nenc message: ', self.rsa.get_enc_message(), '\ndec message: ', self.rsa.get_dec_message())

    def test_work_RSA_2(self):
        self.assertEqual(self.rsa.launch_RSA(secret=2040), 2040)
        print('N = ', self.rsa.get_N(), '\np,q = ', self.rsa.get_p_q(),
              '\npublic key e = ', self.rsa.get_public_key_e(), '\nprivate key d: ', self.rsa.get_d(),
              '\nsecret: ', self.rsa.get_secret(),
              '\nenc message: ', self.rsa.get_enc_message(), '\ndec message: ', self.rsa.get_dec_message())

    def test_symbol_Jacobi(self):
        self.assertEqual(self.rsa.symbol_Jacobi(-104, 997), -1)

    def test_Solovey_Shtrassen(self):
        self.assertEqual(self.rsa.Solovey_Shtrassen(12), False)
        self.assertEqual(self.rsa.Solovey_Shtrassen(3571), True)

    def test_gcd(self):
        self.assertEqual(self.rsa.gcd(12, 6), 6)

    def test_inverse_value(self):
        self.assertEqual(self.rsa.inverse(5, 12), 5)

    def test_Shamir_1(self):
        self.assertEqual(self.shamir1.check(), 43)
    #
    # def test_Shamir_2(self):
    #     self.assertEqual(self.shamir2.check(), 211)
    #
    # def test_Shamir_3(self):
    #     self.assertEqual(self.shamir3.check(), 311)

# еще тесты
if __name__ == "__main__":
    unittest.main()
