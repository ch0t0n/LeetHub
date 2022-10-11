class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        st = []
        for c in s:
            if c == '(' or c == '{' or c=='[':
                st.append(c)
            if c == ')':
                if len(st) == 0:
                    return False
                tp = st.pop()
                if tp != '(':
                    return False
            elif c == '}':
                if len(st) == 0:
                    return False
                tp = st.pop()
                if tp != '{':
                    return False
            elif c == ']':
                if len(st) == 0:
                    return False
                tp = st.pop()
                if tp != '[':
                    return False
        if len(st)==0:
            return True
        
        