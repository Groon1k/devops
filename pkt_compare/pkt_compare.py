from scapy.all import *


def find_pkt(traffic):
    valid_flags = ['S', 'PFU']
    packets = PcapReader(traffic)
    for pkt in packets:
        if pkt[TCP].flags in valid_flags:
            return pkt


pcaps = [
    'the_first.pcap',
    'the_second.pcap',
    'the_third.pcap']

pkts = list(map(find_pkt, pcaps))

for osi in range(0, 7):
    try:
        layer = pkts[0].getlayer(osi).name
        print(f"\nLAYER {osi+1} - {layer}")
    except AttributeError as e:
        print("\nDone with layers")
        break
    fields = list(pkts[0][layer].fields.keys())
    for pole in fields:
        values = [pkt[layer].fields.get(pole) for pkt in pkts]
        try:
            unique_values = set(values)
            if len(unique_values) != 1:
                print(pole, values)
        except TypeError as e:
# unhashable type list ([],[],[])
            pass
