import random

message = input("Enter message: ")
fillers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,./;#[]!"£$%^&*()/?@'
arr = list(message)
arrFillers = list(fillers)
x = len(message)
i = 0
encrypt = []
decrypt = []

# Hides the value of input by converting each letter to their decimal ASCII value while adding random characters between
for i in range(x):      
    encrypt.append(ord(arr[i]))
    encrypt.append(random.choice(arrFillers))
    i += 1

encryptedMessage = "".join(map(str, encrypt))
print("Encryption Is: " + encryptedMessage) # shows Encrypted message
newArr = list(encryptedMessage)
encryptedMessage = "".join(map(str, newArr))

# Decrypts the encrypted string to just the ASCII code format
y = len(fillers)
for i in range(y):
    encryptedMessage = encryptedMessage.replace(fillers[i], ',')
    i += 1
finArr = encryptedMessage.split(',')
finArr.pop()
finArrlist = list(finArr)   

# Converts the ASCII code back to the original message
z = len(finArrlist)
for i in range(z):
    decrypt.append(chr(int(finArr[i]))) 
    i += 1
final = "".join(map(str, decrypt))
print("Decrypted: " + final)

