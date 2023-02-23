print("Введите номер билета")
billet = int(input())
a = billet/100000
b = (billet/10000)%10
c = (billet/1000)%10
print("Yes" if int(billet/100000) + int((billet/10000)%10) + int((billet/1000)%10) == 
      int(billet%10) + int((billet%100)/10) + int((billet%1000)/100) else "No")