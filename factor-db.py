WARNINGS = 0;
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[97m'
    RED = '\033[96m'
    LIGHT = '\033[95m'

    
try: 
	import re
	import requests
	from bs4 import BeautifulSoup 
	import sys
	import os
except Exception as err:
	print "[!] "+str(err)
	sys.exit(0)



status ={"C" :"Composite, no factors known",
         "CF":"Composite, factors known",
         "FF":"Composite, fully factored" ,
         "P" : "Definitely prime" ,
         "Prp": "Probably prime" ,
         "U" : "Unknown" ,
         "Unit": "Just for 1" ,
         "N" : "This number is not in database (and was not added due to your settings)" ,
         "*" : "Added to database during this request"}

baseUrl = "https://factordb.com/"
def banner():
    print bcolors.HEADER + " / _| __ _  ___| |_ ___  _ __       __| | |_ "+bcolors.ENDC
    print bcolors.HEADER + " | |_ / _` |/ __| __/ _ \| '__|____ / _` | '_ \ "+bcolors.ENDC
    print bcolors.HEADER + " |  _| (_| | (__| || (_) | | |_____| (_| | |_) | "+bcolors.ENDC
    print bcolors.HEADER + " |_|  \__,_|\___|\__\___/|_|        \__,_|_.__/  "+ bcolors.ENDC
    print bcolors.LIGHT + "================> https://github.com/p4r4xor/rsa-tool"
    print bcolors.OKBLUE+ "================> made with love by AR.\n"

def usage():
    scr = os.path.basename(sys.argv[0])
    banner()
    print bcolors.WARNING +"Usage: python factordb.py {n}  \n"



def interact(n):
    myVars = []
    r = requests.get(baseUrl+"index.php?query="+n)
    html = r.content
    mylist =[]
    soup = BeautifulSoup(html,"lxml")
    tables = soup.findAll("table")
    for table in tables:
         if table.findParent("table") is None:
            for row in table.findAll("tr"):
                cells = row.findAll("td")
                mylist.append(str(cells))
    data = mylist[3]
    data = data.split(",")
    soup2 = BeautifulSoup(data[0],"lxml")
    for row in soup2.findAll("td"):
        status = row.text # Get the status

    links = []
    soupLinks = BeautifulSoup(data[2],"lxml")
    for row in soupLinks.findAll("a"):
        links.append(row["href"])
    l = len(links)
    myVars.append([status,links[l-2],links[l-1]])
    return myVars


def get_prime(p):
    r = requests.get(baseUrl+p)
    html = r.content
    soup = BeautifulSoup(html,"lxml")
    try:
        value = soup.find('input', {'name': 'query'}).get('value')
        return value
    except:
        print "Fail"

def start(argv):
    if len(sys.argv) < 2:
        usage()
        sys.exit()
    else:
        main(argv[0])
        
def main(n):
    s,p ,q = interact(n)[0]
    if p == q:
        banner()
        print bcolors.WHITE +"Status :"+s+" => "+status[s]+"\n"
        print bcolors.HEADER+"n : "+n +"\n"
        print bcolors.OKBLUE +"length : "+str(len(n))+"\n"
    else :
        P = get_prime(p)
        Q = get_prime(q) 
        banner()
        print bcolors.WHITE +"Status :"+s+" => "+status[s]+"\n"
        print bcolors.RED+" n: {n} \n length : {len} \n".format(n= n,len=len(n))
        print bcolors.WARNING+" p: {P} \n length : {len} \n".format(P = P,len=len(P))
        print bcolors.OKGREEN+" q: {Q} \n length : {len} \n".format(Q=Q,len=len(Q))

if __name__ == '__main__':
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt as err:
        print "\n[!] By... :)"
    sys.exit(0)
