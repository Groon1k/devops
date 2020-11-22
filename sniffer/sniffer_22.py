import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = process_sniffed_packet, filter = 'port 22')

def process_sniffed_packet(packet):
    print(packet.summary())

sniff("eth0")
