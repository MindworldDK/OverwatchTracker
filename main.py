import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import os
import platform
import time

URL = "https://overwatchtracker.com/profile/pc/global/GamingLucas-2685" #URL
GOLD_SR = 2000 #GOLD SR
CurrentSystem = platform.system() # Get current system architecture

# Clear screen function

def clearterminal():
    if CurrentSystem == 'Windows':
        os.system('cls')

    if CurrentSystem == 'Linux':
        os.system('clear')

    if CurrentSystem == 'Darwin':
        os.system('clear')



def SR_CHECKER():

    # Get variables from URL

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    CurrentSR_STRING = soup.find(attrs={'value'}).get_text()

    #Convert string
    CurrentSR_INT = CurrentSR_STRING[0:5]

    # Calculate missing SR

    MissingSR = int(GOLD_SR) - int(CurrentSR_INT)

    # Print current specs

    print ('CURRENT SR: ' + CurrentSR_STRING.strip())
    print ('Required SR: ' + str(GOLD_SR))
    print ('You are missing: ' + str(MissingSR))

    # Print goal has been achieved

    if int(CurrentSR_INT) == int(GOLD_SR):
        print('CONGRATULATIONS YOU ARE IN GOLD')

    if int(CurrentSR_INT) > int(GOLD_SR):
        print('CONGRATULATIONS YOU ARE IN GOLD')

while True:
    clearterminal()
    SR_CHECKER()
    time.sleep(15) # Time inverval