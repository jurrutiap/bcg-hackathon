import numpy as np
import utils.globals as g

def default_map(request):
    return 'pk.eyJ1IjoianVycnV0aWFwIiwiYSI6ImNsbmY0YmdjOTBoNGwya3JpbnB3dDN4b3UifQ.U7ld5qVva8zy9ZibouV10g'

def closest_parking_spot(user_address, parking_spots):
    for spot in parking_spots:
        if spot.address == user_address:
            return spot

def k(k):
    try:
        K= int(k)%26
    except:
        K = np.random.randint(26)
    return K

def encrypt(text, K):
    listcrypt= []
    x= g.chartonum(text)
    for i in x:
        listcrypt.append((i+K)%26)
    return g.numtochar(listcrypt)

def desencrypt(text, K):
    listcrypt= []
    x= g.chartonum(text)
    for i in x:
        listcrypt.append((i-K)%26)
    y= g.numtochar(listcrypt)
    return y.upper()

if __name__ == "__main__":
    message = str(input("Message:"))  # "MYSECRETMESSAGE"
    key= k()
    print(encrypt(message,key))