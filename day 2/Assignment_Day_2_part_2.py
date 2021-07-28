#  OTP Generator
import random as r
import string
max_len = 6
union_list = string.ascii_letters + string.digits
otp = ""
for i in range(max_len):
    otp += r.choice(union_list)

print(otp)