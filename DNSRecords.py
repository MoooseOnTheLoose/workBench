import dns.resolver #pip3 install dnspython
def main(domain):
    records = ['A','AAAA','NS','SOA','MX','TXT','CNAME','PTR']
    for record in records:
        try:
            responses = dns.resolver.resolve(domain, record)
            print("\nRecord response ",record)
            print("-----------------------------------")
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
