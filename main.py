import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import os
import platform
import time

URL = "https://overwatchtracker.com/profile/pc/global/GamingLucas-2685"
GOLD_SR = 2000
CurrentSystem = platform.system()

def clearterminal():
    if CurrentSystem == 'Windows':
        os.system('cls')

    if CurrentSystem == 'Linux':
        os.system('clear')

    if CurrentSystem == 'Darwin':
        os.system('clear')



def SR_CHECKER():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    CurrentSR_STRING = soup.find(attrs={'value'}).get_text()
    CurrentSR_INT = CurrentSR_STRING[0:5]

    MissingSR = int(GOLD_SR) - int(CurrentSR_INT)

    print ('CURRENT SR: ' + CurrentSR_STRING.strip())
    print ('Required SR: ' + str(GOLD_SR))
    print ('You are missing: ' + str(MissingSR))

    if CurrentSR_INT == 2500:
        print('CONGRATULATIONS YOU ARE IN GOLD')

    if CurrentSR_INT < 2500:
        print('CONGRATULATIONS YOU ARE IN GOLD')


while True:
    time.sleep(60)
    clearterminal()