import random
# Description of 20 common TCP ports and 20 common UDP ports with a study game.
class Protocol:
    def __init__(self, name, number, description):
        self.name = name
        self.number = number
        self.description = description
    def getProtocolInfo(self):
        print("")
        print(f"{self.name} - {self.number} - {self.description}")
        print("")
#---GLOBALS
LISTTCP = {'FTP':21, 'SSH':22, 'TELNET':23, 'SMPT':25, 'DNS':53, 'HTTP':80, 'POP3':110, 'RPCBIND':111, 'MSRPC':135, 'NETBIOS SSN':139, 'IMAP':143,
           'HTTPS':443, 'MICROSOFT DS':445, 'IMAPS':993, 'POP3S':995, 'PPTP':1723, 'MYSQL':3306, 'MS TERM SERVER':3389, 'VNC':5900, 'HTTP PROXY':8080}
LISTUDP = {'DNS':53,'DHCPS':67, 'DHCPC':68,'TFTP':69, 'NTP':123, 'MSRPC':135, 'NETBIOS NS':137, 'NETBIOS DGM':138, 'NETBIOS SSN':139,
            'SNMP':161, 'SNMPTRAP':162, 'MICROSOFT DS':445, 'ISAKMP':500, 'SYSLOG':514, 'RIP':520, 'IPP':631, 'MS SQL DS':1434, 
            'UPNP':1900, 'NAT T IKE':4500, 'VARIES':49152} 
def main():
    print("")
    questionUser()
       
def questionUser():
    count = 0
    while count <= 3:
        print(('-' * 23))
        ask = input("(G)ame? (Q)uit?" + '\n' + "UDP or TCP ports? ")
        if ask.lower() == "tcp":
            print(('-' * 23))
            tcpPorts()
        elif ask.lower() == "udp":
            print(('-' * 23))
            udpPorts()
        elif ask.lower() == "game" or ask.lower() == "g":
            callGame()
        elif ask.lower() == "q" or ask.lower() == "quit":
                print(('-' * 23))
                exit()    
        else:
            print("Incorrect input. Try again.")
            count += 1    
def tcpPorts():
    ftp = Protocol("FTP", 21, "File Transfer Protocol")
    ssh = Protocol("SSH", 22, "Secure Shell")
    telnet = Protocol("TELNET", 23, "Client/Server Protocol")
    smtp = Protocol("SMTP", 25, "Simple Mail Transfer Protocol")
    dns = Protocol("DNS", 53, "Domain Name Server")
    http = Protocol("HTTP", 80, "Hypertext Transer Protocol (Unsecured)")
    pop3 = Protocol("POP3", 110, "Post Office Protocol Version 3 for email retrieval (insecure)")
    rpcBIND = Protocol("RPCBIND", 111, "Maps SunRPC program numbers to their current TCP or UDP ports")
    msRPC = Protocol("MSRPC", 135, "Common Port For Window Services")
    netBIOSSNN = Protocol("NetBIOS SSN", 139, "Communications for NetBIOS Session Service")
    imap = Protocol("IMAP", 143, "Internet Message Access Protocol version 2")
    https = Protocol("HTTPS", 443, "Hypertext Transfer Protocol Secured")
    msDS = Protocol("MICROSOFT DS", 445, "SMB Over IP With Windows services")
    imaps = Protocol("IMAPv2 SLL", 993, "IMAPv2 with SLL security")
    pop3S = Protocol("POP3 SSL", 995, "POP3 with SSL Security")
    pptp = Protocol("PPTP", 1723, "Point To Point Tunneling Protocol ")
    mySQL = Protocol("MySQL", 3306, "Communication with MySQL databases")
    msTermServer = Protocol("MS TERM SERVER", 3389, "Microsoft Terminal Services port")
    vnc = Protocol("VNC", 5900, "A Graphical Desktop Sharing System")
    httpProxy = Protocol("HTTP PROXY", 8080, "Commonly Used For HTTP Proxies")
    count = 0
    while count <= 3:
        answer = input("(B)ack? (L)ist? (Q)uit? " + '\n' + "-- Which TCP protocol: ")
        if answer.lower() == "ftp" or answer == str(21):
            str(ftp.getProtocolInfo())
            count = 0
        elif answer.lower() == "ssh" or answer == str(22):
            str(ssh.getProtocolInfo())
            count = 0
        elif answer.lower() == "telnet" or answer == str(23):
            str(telnet.getProtocolInfo())
            count = 0
        elif answer.lower() == "smtp" or answer == str(25):
            str(smtp.getProtocolInfo())
            count = 0
        elif answer.lower() == "dns" or answer == str(53):
            str(dns.getProtocolInfo())
            count = 0
        elif answer.lower() == "http" or answer == str(80):
            str(http.getProtocolInfo())
            count = 0
        elif answer.lower() == "pop3" or answer.lower() == "pop 3" or answer == str(110):
            str(pop3.getProtocolInfo())
            count = 0
        elif answer.lower() == "rpc-bind" or answer.lower() == "rpcbind" or answer == str(111):
            str(rpcBIND.getProtocolInfo())
            count = 0
        elif answer.lower() == "msrpc" or answer == str(135):  
            str(msRPC.getProtocolInfo())
            count = 0  
        elif answer.lower() == "netbios-ssn" or answer.lower() == "netbios_ssn" or answer.lower() == "netbiossnn" or answer.lower() == "netbios ssn" or answer == str(139):  
            str(netBIOSSNN.getProtocolInfo())
            count = 0  
        elif answer.lower() == "imap" or answer == str(143):  
            str(imap.getProtocolInfo())
            count = 0  
        elif answer.lower() == "https" or answer == str(443):
            str(https.getProtocolInfo())
            count = 0           
        elif answer.lower() == answer.lower() == "microsoft-ds" or answer.lower() == "microsoft_ds" or answer.lower() == "microsoft ds" or answer.lower() == "microsoftds" or answer == str(445):
            str(msDS.getProtocolInfo())
            count = 0
        elif answer.lower() == "pop3s" or answer.lower() == "pop ssl" or answer == str(995):  
            str(pop3S.getProtocolInfo())
            count = 0 
        elif answer.lower() == "imaps" or answer == str(993):  
            str(imaps.getProtocolInfo())
            count = 0   
        elif answer.lower() == "pptp" or answer == str(1723):  
            str(pptp.getProtocolInfo())
            count = 0     
        elif answer.lower() == "my-sql" or answer.lower() == "my_sql" or answer.lower() == "my sql" or answer.lower() == "mysql" or answer == str(3306):  
            str(mySQL.getProtocolInfo())
            count = 0             
        elif answer.lower() == "ms-term-server" or answer.lower() == "ms_term_server" or answer.lower() == "ms term server" or answer.lower() == "mstermserver" or answer == str(3389):
            str(msTermServer.getProtocolInfo())
            count = 0  
        elif answer.lower() == "vnc" or answer == str(5200):  
            str(vnc.getProtocolInfo())
            count = 0     
        elif answer.lower() == "http-proxy" or answer.lower() == "http_proxy" or answer.lower() == ("http proxy") or answer.lower() == ("httpproxy") or answer == str(8080):  
            str(httpProxy.getProtocolInfo())
            count = 0
        elif answer.lower() == "b":
            questionUser()
        elif answer.lower() == "list" or answer.lower() == "l":
            print("")
            for key, value in LISTTCP.items():
                print(key, value)   
            print(" ")          
        elif answer.lower() == "q" or answer.lower() == "quit":
            print(('-' * 23))
            exit()
        else:
            print("Incorrect input. Try again")
            count += 1
def udpPorts():
    dns = Protocol("DNS", 53, "Domain Name Systems Server")
    dhcps = Protocol("DHCPS", 67, "Dynamic Host Configuration Protocol Server")
    dhcpc = Protocol("DHCPC", 68, "DHCP Client port")
    tftp = Protocol("TFTP", 69, "Trivial File Transfer Protocol")
    ntp = Protocol("NTP", 123, "Network Time Protocol")
    msRPC = Protocol("MS RPC", 135, "Windows Services Port")
    netBIOSNS = Protocol("NETBIOS NS", 137, "UDP Port For Windows")
    netBIOSDGM = Protocol("NETBIOS DGM", 138, "Another Windows Service")
    netBIOSSSN = Protocol("NETBIOS SSN", 139, "Another Windows Service")
    snmp = Protocol("SNMP", 161 ,"Simple Network Manage Protocol")
    snmpTrap = Protocol("SNMPTRAP", 162, "Simple Network Management Protocol")
    msDS = Protocol("MS DS", 445, "Windows Services Port")
    isakmp = Protocol("ISAKMP", 500, "Internet Seurity Association And Key Management")
    sysLog = Protocol("SYSLOG", 514, "Standard UNIX Log Daemon")
    rip = Protocol("RIP", 520, "Routing Information Protocol")
    ipp = Protocol("IPP", 631, "Internet Printing Protocol")
    msSQLDS = Protocol("MS SQL DS", 1434, "Microsoft SQL")
    upnp = Protocol("UPNP", 1900, "Microsoft Simple Service Discovery Protocol")
    natTIKE = Protocol("NAT T TIKE", 4500,"Network Address Translation during IP Sec Key Exchange")
    ephemeral = Protocol("Varies", 49152, "First Ephemeral Port The First Program Connects Too")
    count = 0
    while count <= 3:
        answer = input("(B)ack? (L)ist? (Q)uit?" + '\n' + "-- Which UDP protocol: ")
        if answer.lower() == "dns" or answer == str(53):
            str(dns.getProtocolInfo())
            count = 0
        elif answer.lower() == "dhcps" or answer == str(67):
            str(dhcps.getProtocolInfo())
            count = 0
        elif answer.lower() == "dhcps" or answer == str(68):
            str(dhcpc.getProtocolInfo())
            count = 0
        elif answer.lower() == "tftp" or answer == str(69):
            str(tftp.getProtocolInfo())
            count = 0         
        elif answer.lower() == "ntp" or answer == str(123):
            str(ntp.getProtocolInfo())
            count = 0
        elif answer.lower() == "ntp" or answer == str(135):
            str(msRPC.getProtocolInfo())
            count = 0    
        elif answer.lower() == "netbios ns" or answer == str(137):
            str(netBIOSNS.getProtocolInfo())
            count = 0        
        elif answer.lower() == "netbios dgm" or answer == str(138):
            str(netBIOSDGM.getProtocolInfo())
            count = 0
        elif answer.lower() == "netbios ssn" or answer == str(139):
            str(netBIOSSSN.getProtocolInfo())
            count = 0      
        elif answer.lower() == "snmp" or answer == str(161):
            str(snmp.getProtocolInfo())
            count = 0
        elif answer.lower() == "snmptrap" or answer == str(162):
            str(snmpTrap.getProtocolInfo())
            count = 0
        elif answer.lower() == "msds" or answer == str(445):
            str(msDS.getProtocolInfo())
            count = 0 
        elif answer.lower() == "isakmp" or answer == str(500):
            str(isakmp.getProtocolInfo())
            count = 0
        elif answer.lower() == "syslog" or answer == str(514):
            str(sysLog.getProtocolInfo())
            count = 0
        elif answer.lower() == "isakmp" or answer == str(520):
            str(rip.getProtocolInfo())
            count = 0              
        elif answer.lower() == "ipp" or answer == str(631):
            str(ipp.getProtocolInfo())
            count = 0
        elif answer.lower() == "ms sql ds" or answer == str(1434):
            str(msSQLDS.getProtocolInfo())
            count = 0
        elif answer.lower() == "upnp" or answer == str(1900):
            str(upnp.getProtocolInfo())
            count = 0
        elif answer.lower() == "nat t ike" or answer == str(4500):
            str(natTIKE.getProtocolInfo())
            count = 0
        elif answer.lower() == "emphemeral" or answer == str(49152):
            str(ephemeral.getProtocolInfo())
            count = 0 
        elif answer.lower() == "b":
            questionUser() 
        elif answer.lower() == "list" or answer.lower() == "l":
            print("")
            for key, value in LISTUDP.items():
                print(key, value)
            print(" ")  
        elif answer.lower() == "q" or answer.lower() == "quit":
            print(('-' * 23))
            exit()
        else:
            print("Incorrect input. Try again")
            count += 1
def callGame():
    print("")
    count = 0
    while count <= 3:
        ask = input("(P)lay? (B)ack?" + '\n')
        if ask.lower() == "p" or ask.lower() == "play": 
            tcpUDP = random.randint(1, 2)
            if tcpUDP == 1:
                question = random.choice(list(LISTTCP.values()))
                answer = input(f"What is TCP port {question} ? " )
                print("The answer is: " + list(LISTTCP.keys())[list(LISTTCP.values()).index(question)] + ".")
                callGame()
            else:
                question = random.choice(list(LISTUDP.values()))
                answer = input(f"What is UDP port {question} ? " )
                print("The answer is: " + list(LISTUDP.keys())[list(LISTUDP.values()).index(question)] + ".")
                callGame()         
        elif ask.lower() == "b" or ask.lower() == "back":
            questionUser()
        else:
            print("Incorrect input. Try again")
            count += 1
                            
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()      
