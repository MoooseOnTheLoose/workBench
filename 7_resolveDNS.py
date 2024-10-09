import dns.resolver #pip3 install dnspython
'''    
Records 
MAIL SERVERS = MX
NAMER SERVERS = NS
IPv4 ADDRESS = A
IPv6 ADDRESS = AAA
'''
def main():
    resolveDNS()    
def resolveDNS():
    hosts = ["google.com", "microsoft.com"] # Insert target host here
    for host in hosts:
        print("\n" + host)
        ip = dns.resolver.resolve(host, "NS") # Insert desired record here 
        for i in ip:
            print(i)      
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
