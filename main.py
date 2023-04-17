import random
from zxcvbn import zxcvbn


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + numbers + symbols

while True:
 user_input = input("Qual o tamanho da Senha? ")

 try:
    pass_length = int(user_input)
 except ValueError:
    print("Digite um valor válido! ")
    break



 Password = "" .join(random.sample(Use_for, pass_length))

 results = zxcvbn(Password)

 print("A senha gerada foi: " + Password)
 print("===============")
 print(results)
 break



