class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        parens = {'{':'}','[':']','(':')'}
        for i in s:
            if i in parens.keys():
                st.append(i)
            elif i in parens.values():
                if len(st)==0 or parens[st[-1]]!=i:
                    return False
                else:
                    st.pop()
            else:
                return False
        return len(st)==0