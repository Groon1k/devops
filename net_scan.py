import scapy.all as scapy
import optparse

def get_arg():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP / IP range")
    (opt, arg) = parser.parse_args()
    return opt

    
def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad = broadcast/arp_req
    answ = scapy.srp(arp_req_broad, timeout=5, verbose=False)[0]
    lst = []
    for some in answ:
        dct = {"ip":some[1].psrc, "mac": some[1].hwsrc}     
        lst.append(dct)
    return lst


def print_res(res_lst):
    print("IP\t\t\tMAC Address\n----------------------------------------------------------------------")
    for some in res_lst:
        print(some["ip"] + "\t\t" + some["mac"])


options = get_arg()
scan_res = scan(options.target)
print_res(scan_res)
