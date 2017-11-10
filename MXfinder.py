import dns.resolver
import collections

def get_mx_record(domain_name):
    
    resolver = dns.resolver.Resolver()
    if domain_name:
        result = collections.defaultdict(list)
        domain_name = domain_name.strip()
        mx_recs = resolver.query(domain_name,'MX')
        for mx_rec in mx_recs:
            mx_name = str(mx_rec).split()[1]
            a_recs = resolver.query(mx_name,'A')
            for a_rec in a_recs:
                result[mx_name].append(str(a_rec))
        return result
    
dname = input('Enter a domain name : ')
get_mx_record(dname)
