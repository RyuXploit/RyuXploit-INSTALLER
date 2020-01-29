from googlesearch import search
import requests,sys,json,os
os.system('clear')
banner = '''\x1b[1;31m
__________        __    
\______   \ _____/  |_  
 |    |  _//  _ \   __\ 
 |    |   (  <_> )  |   
 |______  /\____/|__|   
        \/              
\x1b[0m __      __.__ __   .__ 
/  \    /  \__|  | _|__|
\   \/\/   /  |  |/ /  |
 \        /|  |    <|  |
  \__/\  / |__|__|_ \__|
       \/          \/   
'''
print (banner)
query = raw_input("Silahkan Bertanya : ")
quer = query + " inurl:id.wikipedia.org"
a = list(search(quer,num=1, stop=4))
res = a[0].replace("https://id.wikipedia.org/wiki/","").replace("_"," ")
qus = query.split(" ")
for qu in qus:
    if qu.lower() in res.lower():
       res = a[1].replace("https://id.wikipedia.org/wiki/","").replace("_"," ")

for quu in qus:
    if quu.lower() in res.lower():
       res = a[2].replace("https://id.wikipedia.org/wiki/","").replace("_"," ")
ask = raw_input("Tampilkan Info ? (y/n)")
if ask.lower() == "n":
   print (res)
   sys.exit()

ektr = requests.get("https://id.wikipedia.org/api/rest_v1/page/summary/"+res.replace(" ","_")).text
ektr = json.loads(ektr)
penjelasan = ektr['extract']
print
print(res)
print(penjelasan)
print


#sesuai perkataan yakan:v

