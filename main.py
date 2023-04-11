import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + number + symbols
pass_length = int(input("Qual tamanho da senha?"))

Password = "" .join(random.sample(Use_for, pass_length))

print("A senha gerada é : "+ Password)