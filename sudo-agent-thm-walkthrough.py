import requests
import pyfiglet
import sys
import string
import platform

def logo():
     text = 'Sudo Agent THM'
     banner = pyfiglet.figlet_format(text,width=200)
     print(f'\033[0;32m{banner}\033[0;0m\t\t\t\t\t Sudo Agent TryHackMe Walkthrough')
     print('')

def check_os():
     _what_os = platform.system()
     return _what_os

def taken_url_from_user():
     url = input('[+] Enter URL or IP:>\033[0;32m ')
     print('\033[0;37m')
     if ' ' in url:
          print('White space is not allowed in URL! Please enter valid URL...')
          sys.exit()
     elif url.startswith('http') or url.startswith('https'):
          return url
     else:
          return 'http://' + url

def create_user_agent_wordlist():
     alphabets = []
     lower_case = string.ascii_lowercase
     upper_case = string.ascii_uppercase
     alpha_collection = lower_case + upper_case
     for i in alpha_collection:
          alphabets.append(i) 
     return alphabets
     
def dump_data_from_site(urls,alphabets):
     for i in range(len(alphabets)):
          try:
               r = requests.get(urls,headers={'User-Agent':alphabets[i]})
               r.raise_for_status()
               
               if r.status_code == 200:
                    if '!DocType' in r.text:
                         print(f'{urls}/User-Agent:{alphabets[i]}')
                         continue
                    else:
                         print(r.text)
                         break  
                     
          except requests.exceptions.HTTPError as e:
               print(e)
          except requests.exceptions.ConnectionError as e:
               print(e)
          except requests.exceptions.Timeout as e:
               print(e)
          except requests.exceptions.RequestException as e:
               print(e)
          except Exception as e:
               print(e)

def main():
     """_summary_
     Author:   Ravi Kumar
     Date:     03-03-2024
     version:  1.0.0
     """     
     
     logo()
     what_os = check_os()
     if what_os == 'Linux' or what_os == 'Posix':
          validUrl = taken_url_from_user()
          alpha = create_user_agent_wordlist()
          dump_data_from_site(validUrl,alpha)
     else:
          print('Not supported!')
               
if __name__ == '__main__':
     main()