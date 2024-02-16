class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        def add_to_hm(domain, count):
            if domain in hm: hm[domain] += count
            else: hm[domain] = count

        hm = {}
        result = []

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            domain_list = domain.split('.')
            count = int(count)
            
            add_to_hm(domain, count)
            if len(domain_list) == 3:
                middle_domain = domain_list[1] + "." + domain_list[2]
                add_to_hm(middle_domain, count)
            add_to_hm(domain_list[-1], count)

        for domain, count in hm.items():
            result.append(str(count) + " " + domain)

        return result