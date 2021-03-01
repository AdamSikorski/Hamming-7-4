"""
1)Bity na wejœciu dla stringa "Adam"
0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,1,1,0,1
2)W przyk³adzie przek³amuje pierwszy bit w pierwszej tablicy ktora wychodzi z outputu funkcji Hamming 7.4:
1,0,0,1,1,0,0  ----> 0,0,0,1,1,0,0
3) Output demodulacji:
Rozpoznanie przeklamanego bitu ( pozycja 1)
Bity na wyjœciu:
0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,1,1,0,1
"""
#  funkcia S2BS uproszczona dla tej laborki
def S2BS( napis ):
  b = [bin(ord(x))[2:].zfill(8) for x in napis]
  global zwracana_wartosc
  for x in b:
    zwracana_wartosc = "".join(b)
  return (zwracana_wartosc)

napiss = input("Podaj napis: ")
S2BS(napiss)

# zad1 - funkcja hamminga

X = []

for i in range(len(zwracana_wartosc)):
  if zwracana_wartosc[i] =='1':
    X.append(1)
  if zwracana_wartosc[i] =='0':
    X.append(0)

#X = Array(X)
print("Bity na wejœciu: ")
print("",X)

import numpy as np

def Hamming74():
  G  = np.array([(1,1,0,1), (1,0,1,1),(1,0,0,0),(0,1,1,1),(0,1,0,0),(0,0,1,0),(0,0,0,1)])
 
  pakiet = np.zeros( (int(len(X)/4), 4) )
  global h
  h = []
 
  for i in range(0,len(pakiet),1): 
    for j in range(0,4,1): 
      pakiet[i][j] = X[j+4*i]
    hh = np.array(G.dot(pakiet[i])%2,dtype = np.uint64)
    h.append(hh)
  return h

h = Hamming74()
#print(h[0])
print("Przed przek³amaniem: ")
print("",h[0])
def negacja(Xx,w1,w2):
  if Xx[w1][w2] == 0:
    Xx[w1][w2] = 1
  else:
    Xx[w1][w2] = 0
  return Xx

negacja(h,0,0)
print("Przyk³adowo przek³amuje 1 bit w 1 czesci:")
print("Po przek³amaniu: \n",h[0])
print("Za pomoc¹ demodulacji odnajduje pozycjê przek³amanego bitu i zwracam to co w inpucie: ")
def demodulacja74():
  wektor_wyjsciowy = []
  for i in range(0,len(h),1): # d³ugosc h (ilosc tablic)
    p1 = (h[i][0] + h[i][2] + h[i][4] + h[i][6]) % 2 
    p2 = (h[i][1] + h[i][2] + h[i][5] + h[i][6]) % 2
    p3 = (h[i][3] + h[i][4] + h[i][5] + h[i][6]) % 2
    n = p1 *2**0 + p2*2**1 + p3*2**2
    n = int(n)
    if n == 0:
      wektor_wyjsciowy.append(int(h[i][2]))
      wektor_wyjsciowy.append(int(h[i][4]))
      wektor_wyjsciowy.append(int(h[i][5]))
      wektor_wyjsciowy.append(int(h[i][6]))
    if n > 0:
      if h[i][n] == 1:
        h[i][n] = 0
      else:
        h[i][n] = 1
      print("Blad na indeksie: ", n)
      wektor_wyjsciowy.append(int(h[i][2]))
      wektor_wyjsciowy.append(int(h[i][4]))
      wektor_wyjsciowy.append(int(h[i][5]))
      wektor_wyjsciowy.append(int(h[i][6]))
  return wektor_wyjsciowy

test = demodulacja74()
print("Bity na wyjœciu: ")
print("",test)

