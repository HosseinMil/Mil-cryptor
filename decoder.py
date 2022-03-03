import os, sys, design
from colorama import Fore as color
from time import sleep

bold = '\033[1m'
endbold = '\033[0m'

def decoder_menu(user_inp):
    if (user_inp == 1):
        os.system('clear');design.banner()
        print(color.WHITE+"Enter Your Encrypted text in base64:")
        user_option = input(color.RED+"\n[♦] "+color.RED+"Mil.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+"base64_Dcryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ♦ ")
        os.system(f'echo {user_option} | base64 -d')
        input('\n press any key ....'+endbold)
    elif (user_inp == 2):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[♦] "+color.RED+"Mil.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+"Hex_Dcryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ♦ ")
            print(bold+color.WHITE+"Encrypted ♦\n ")
            os.system(f'echo {user_option} | xxd -p -r')
            input("\nPress Any Key...."+endbold)
    elif (user_inp == 3):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[♦] "+color.RED+"Mil.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+"Rot13_Dcryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ♦ ")
            print(bold+color.WHITE+"Encrypted ♦\n ")
            os.system(f"echo {user_option} | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
            input("\nPress Any Key...."+endbold)
    elif (user_inp == 0):
        pass
    else:
        print("print Bad input....")
        sleep(1)
        sys.exit()

            
