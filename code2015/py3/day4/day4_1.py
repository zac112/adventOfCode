import hashlib

secretHash = "bgvyzdsv"

number = 0
while True:
    m = hashlib.md5()
    m.update((secretHash+str(number)).encode('utf-8'))
    d = m.hexdigest()
    if str(d).startswith("00000"):
        print (number)
        break
    number += 1
