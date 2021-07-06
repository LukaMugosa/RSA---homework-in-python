import os
import tkinter as tk
from stringRSA import *
from mathRSA import *

window = tk.Tk()
window.geometry("1000x700")
window.title("RSA Enkripcija-Dekripcija")
# ----------

label1 = tk.Label(window, text="Ulaz", bg="lightgray")
label1.place(x=520, y=0, height=30, width=50)
###-----------

label2 = tk.Label(window,
                  text="Ulaz je k-zeljeni broj cifara za koji se mogu provjeriti metodi Setuj Rsa i Pronadji Proste",
                  bg="lightblue")
label2.place(x=200, y=180, height=150, width=600)

# ----------
label3 = tk.Label(window, text="Poruka", bg="lightgray")
label3.place(x=375, y=0, height=30, width=50)
###-----------
# ----------
label4 = tk.Label(window, text="Izlaz -->>>>", bg="lightgray")
label4.place(x=200, y=500, height=30, width=100)
# ----------------
message1 = tk.Entry()
message1.place(x=505, y=35, height=40, width=80)
# ----------------
###-----------

###-----------
message = tk.Text()  ###poruka
message.place(x=300, y=35, height=100, width=200)
# ----------------

global N
N = 0
global p
p = 0
global q
q = 0
global e
e = 0
global d
d = 0


def rsa_set():
    nnn = int(message1.get())
    pp = prim_numfind(nnn, 0)
    qq = prim_numfind(nnn, pp + 1)
    NN = pp * qq
    phi = (pp - 1) * (qq - 1)
    ee = random.randrange(1, phi)
    gg = gcd(ee, phi)
    # ---
    while gg != 1:
        ee = random.randrange(1, phi)
        gg = gcd(ee, phi)
    # ----
    dd = multiplicative_inverse(ee, phi)
    stringg = "N={} ,p={} ,q={} ,e={} ,d={} ,phi={} .".format(NN, pp, qq, ee, dd, phi)
    results.delete("1.0", "end")
    results.insert("1.0", stringg)
    k = [NN, pp, qq, ee, dd]
    global N
    N = NN
    global p
    p = pp
    global q
    q = qq
    global e
    e = ee
    global d
    d = dd
    return k


# -------------

def enccrypt():
    msg = message.get("1.0", "end-1c")
    s = rsa_set()
    global N
    global e
    NN = N
    ee = e
    key = (NN, ee)
    codedMsg = transform(msg, key, True)
    # codedMsg = encrypt11(key,N)
    results.delete("1.0", "end")
    results.insert("1.0", codedMsg)


# ----------------------------------
# ------------------------------------------------
button1 = tk.Button(window, text="Enkriptuj", command=enccrypt, bg="darkgray")
button1.place(x=450, y=150, height=30, width=50)


def decrypttt():
    msgDecodee = results.get("1.0", "end-1c")
    results.delete("1.0", "end")
    global N
    global d
    Nn = N
    dd = d
    key = (Nn, dd)
    decoding = transform(msgDecodee, key, False)
    # decoding = decrypt22(key,msgDecodee)

    results.insert("1.0", decoding)


button3 = tk.Button(window, text="Dekriptuj", command=decrypttt, bg="darkgray")
button3.place(x=450, y=370, height=30, width=50)


# -----------------------------------------------

def isPrime():
    nnn = int(message1.get())
    prime = prim_numfind(nnn, 0)
    nn = prime - pow(10, nnn - 1) + 1
    prime2 = prim_numfind(nnn, nn)
    x = "Prime1 = {} , Prime2 = {} .".format(prime, prime2)
    results.delete("1.0", "end")
    results.insert("1.0", x)


# ------------------------------------------------
checkisPrime = tk.Button(window, text="Pronadji Proste", command=isPrime, bg="darkgray")
checkisPrime.place(x=600, y=30, height=20, width=100)
###---------------

# -------------------
# --------------
rsaset = tk.Button(window, text="Setuj RSA", command=rsa_set, bg="darkgray")
rsaset.place(x=600, y=60, height=20, width=100)

# ---------------
results = tk.Text()
results.place(x=330, y=400, height=200, width=300)
# ------------
window.mainloop()


# ----------------
# ------


def main():
    os.system("cls")
    return 0


main()
