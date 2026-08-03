import random
import string
password = ''.join(
    random.choice(
       string.ascii_letters + string.digits
    )for i in range(5)
)
print(password)