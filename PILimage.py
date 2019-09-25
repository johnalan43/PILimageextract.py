#! /usr/bin/env python
#Written by Johnnyz187
#https://www.hackthebox.eu/home/users/profile/92341

from PIL import Image

#This will extract RGB data 
im = Image.open("PNG/JPEG FILE")
pix = im.load()
arr = []
ans = []
 
first = 0
last = 29
while first*10+5 < 135:
 for i in range(first, last+1):
   arr.append(pix[i*10+5,first*10+5])
 for i in range(first+1, last+1):
   arr.append(pix[last*10+5,i*10+5])
 for i in reversed(range(first, last)):
   arr.append(pix[i*10+5,last*10+5])
 for i in reversed(range(first+2, last)):
   arr.append(pix[first*10+5,i*10+5])
 arr.append(pix[(first+1)*10+5,(first+2)*10+5])
 first += 2
 last -= 2
 
arr.append(pix[145,145])
arr.append(pix[155,145])
arr.append(pix[155,155])
 
for i in range(len(arr)):
 temp = 0
 for j in range(3):
   if arr[i][j] == 192:
     temp += 1*(3**(2-j))
   if arr[i][j] == 255:
     temp += 2*(3**(2-j))
 ans.append(chr(97+((temp+12)%26))) #Base3 + ROT+13
 
string = "".join(ans)

string = string.replace("", "_")
string = string.replace("", "{")
string = string.replace("", "}")
string = string.replace("", "!")
string = string.replace("l", "")
while string.find("") != -1:
 array = list(string)
 array[string.find("")+9] = array[string.find("")+9].upper()
 string = "".join(array)
 string = string.replace("", "", 1)

print(string)


