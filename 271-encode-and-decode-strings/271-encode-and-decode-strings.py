class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res+str(len(s))+"$"+s
        return res
                
    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while(i<len(s)):
            curr_count = ""
            while(s[i]!='$'):
                curr_count +=s[i]
                i+=1
            curr_count = int(curr_count)
            curr_word = ""
            i = i+1
            limit = i+curr_count
            while(i<limit):
                curr_word+= s[i]
                i=i+1
            res.append(curr_word)
        return res
            
                


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))