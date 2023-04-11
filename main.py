import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + numbers + symbols
pass_length = 8


Password = "" .join(random.sample(Use_for, pass_length))

print("A senha gerada é : "+ Password)
