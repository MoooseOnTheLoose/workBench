import dns.reversename #pip3 install dnspython
def main():
    reverseDNS()
def reverseDNS():
    domain = dns.reversename.from_address("142.250.31.101")
    print("-"*36)
    print(domain)
    print(dns.reversename.to_address(domain))
    print("-"*36)  
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
