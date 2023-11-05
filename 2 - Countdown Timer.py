import time

def Süre(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Süre Bitti!")

t = input("Saniye Giriniz: ")

Süre(int(t))