class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        results = defaultdict(int)
        def subdomainsOfDomain(domain):
            parts = domain.split(".")
            result = [".".join(parts[i:]) for i in range(len(parts))]
            return result
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            subdomains = subdomainsOfDomain(domain)
            for sub in subdomains:
                results[sub] += int(count)

        return [" ".join([str(results[sub]), sub]) for sub in results.keys()]
