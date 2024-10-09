import dns.resolver #pip3 install dnspython
'''    
Records 
IPv4 ADDRESS = A
IPv6 ADDRESS = AAAA
Canonical Name = CNAME
MAIL SERVERS = MX
NAMER SERVERS = NS
Pointer Record = PTR
State of Authority = SOA
Text = txt
'''
def main(domain):
    records = ['A','AAAA','CNAME','MX','NS','PTR','SOA','TXT']
    for record in records:
        try:
            responses = dns.resolver.resolve(domain, record)
            print("\nRecord response ",record)
            print("-" * 63)
            for response in responses:
                print(response)
        except Exception as exception:
            print("Cannot resolve query for record", record)
            print("Error for obtaining record information:", exception)
if __name__ == '__main__':
	try:
		main('google.com') # Input target host here
	except KeyboardInterrupt:
		exit()
