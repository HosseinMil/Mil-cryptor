from colorama import Fore as color 
from time import sleep
bold = '\033[1m'
endbold = '\033[0m'
def banner():
    print(color.GREEN+'''
 

                                            
  __  __   _   _                         _              
 |  \/  | (_) | |                       | |             
 | \  / |  _  | |   ___ _ __ _   _ _ __ | |_ ___  _ __  
 | |\/| | | | | |  / __| '__| | | | '_ \| __/ _ \| '__| 
 | |  | | | | | | | (__| |  | |_| | |_) | || (_) | |    
 |_|  |_| |_| |_|  \___|_|   \__, | .__/ \__\___/|_|    
                              __/ | |                   
                             |___/|_|                   Base64 | Hex | rot 13 
    
    ''')
    print(bold+color.LIGHTGREEN_EX+'''
  ---------------------------------------
   ♦ Developer : Hossein_Mil            ♦
   ♦ Email  :  iho3ein2000@outlook.com  ♦
  ---------------------------------------
  '''+endbold)
sleep(0.5)

def menu():
  print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Base64")
  print(color.CYAN+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[2]" +color.LIGHTYELLOW_EX+" Hex")
  print(color.CYAN+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[3]"+color.LIGHTYELLOW_EX+" Rot 13")
  print(color.CYAN+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[4]"+color.LIGHTYELLOW_EX+" Decoder")
  print(color.CYAN+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[0]"+color.LIGHTYELLOW_EX+" exit")
  print(color.CYAN+"*********************"+endbold)


def decoder_menu():
  print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Base64")
  print(color.CYAN+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[2]" +color.LIGHTYELLOW_EX+" Hex")
  print(color.CYAN+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[3]"+color.LIGHTYELLOW_EX+" Rot 13")
  print(color.CYAN+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[0]"+color.LIGHTYELLOW_EX+" back")
  print(color.CYAN+"*********************"+endbold)


