import dns.reversename #pip3 install dnspython
def main():
    reverseDNS()
def reverseDNS():
    domain = dns.reversename.from_address("172.253.63.100")
    print(domain)
    print(dns.reversename.to_address(domain))  
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
