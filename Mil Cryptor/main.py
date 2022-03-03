import os, sys, design, decoder
from colorama import Fore as color
from time import sleep

bold = '\033[1m'
endbold = '\033[1m'


############################

try:
    from colorama import fore as color
except:
    print("install the colorama library")

#############################


while True:
    os.system('clear')
    try:
        os.system('clear');design.banner();design.menu()
        option = int(input(color.RED+"\n[♦] "+color.RED+"Mil.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ♦ "))
    #CHECK FOR OPTION
        if (option == 1):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[♦] "+color.RED+"Mil.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+"base64"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ♦ ")
            print(bold+color.WHITE+"Encrypted ♦\n ")
            os.system(f'echo {user_option} | base64')
            input(bold+color.GREEN+"Press Any Key....")
            continue


        elif (option == 2):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[♦] "+color.RED+"Mil.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+"Hex"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ♦ ")
            print(bold+color.WHITE+"Encrypted ♦\n ")
            os.system(f'echo {user_option} | xxd -p')
            input(bold+color.GREEN+"Press Any Key....")
            continue
        elif (option == 3):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[♦] "+color.RED+"Mil.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+"Rot13"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ♦ ")
            print(bold+color.WHITE+"Encrypted ♦\n ")
            os.system(f"echo {user_option} | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
            input(bold+color.GREEN+"Press Any Key....")
            continue
        elif (option == 4):
            os.system('clear');design.banner();design.decoder_menu()
            option = int(input(color.RED+"\n(♦) "+color.RED+"Mil cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"Dcryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ♦ "))  
            decoder.decoder_menu(option)
            continue 
        elif (option == 0):
            print(color.LIGHTCYAN_EX+"THX for using Mil cryptor");sleep(0.5)
            sys.exit()
        else:
            print("Invalid Input :/ ")
            sleep(0.5);sys.exit()
    except:
        sys.exit()

