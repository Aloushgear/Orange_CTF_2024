from collections import Counter
import re

chemin='challenge_1_access.log'
ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')

with open(chemin, 'r') as file:
    ips = [ip_pattern.match(line).group(1) for line in file if ip_pattern.match(line)]

ip_counts = Counter(ips)

top_4_ips = [ip for ip, _ in ip_counts.most_common(4)]

flag = f"OCI_{{{'_'.join(top_4_ips)}}}"
print(flag)

