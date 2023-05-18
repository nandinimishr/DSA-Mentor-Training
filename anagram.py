from collections import defaultdict

class Solution:
	def search(self,pat, txt):
        n, k = len(txt), len(pat)
        
        d = defaultdict(int)
        for i in pat:
            d[i] += 1
        
        count = len(d)
        i = 0
        j = 0
        
        anagrams = 0
        while i <= n-1:
            d[txt[i]] -= 1
            if d[txt[i]] == 0: count -= 1
            if i < k-1:
                i += 1
            else:
                if count == 0: anagrams += 1
                if d[txt[j]] == 0: count += 1
                d[txt[j]] += 1
                i += 1
                j += 1
        return anagrams
