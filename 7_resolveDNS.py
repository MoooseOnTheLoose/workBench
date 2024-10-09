import dns.resolver #pip3 install dnspython
'''    
Records 
MAIL SERVERS = MX
NAMER SERVERS = NS
IPv4 ADDRESS = A
IPv6 ADDRESS = AAAA
'''
def main():
    resolveDNS()    
def resolveDNS():
    hosts = ["google.com", "microsoft.com"]
    for host in hosts:
        print("\n" + host)
        print("-" * 36)
        ip = dns.resolver.resolve(host, "AAAA") 
        for i in ip:
            print(i) 
        print("-" * 36)     
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
