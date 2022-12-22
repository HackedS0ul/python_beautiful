#implement directory browsing..
from main import getData


vuln_endpoints = 'vuln.txt'

if getData():
    #start bruteforce for directories
    for i in vuln_endpoints:
        print("[*] Searcing for vulnerabilities..")
        if i not in getData():
            print("[-] Website is not vulnerable")
        else:
            print("[+] Found url " + vuln_endpoints)
else:
    print("Not found data file ")