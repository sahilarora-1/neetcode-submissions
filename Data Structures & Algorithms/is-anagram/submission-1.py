class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        def quick_sort(chars : list)->list:
            if len(chars)<=1:
                return chars
            pivot=chars[len(chars)//2]

            left=[]
            for x in chars:
                if x<pivot:
                    left.append(x)
            middle=[]
            for x in chars:
                if x==pivot:
                    middle.append(x)
            right=[]
            for x in chars:
                if x>pivot:
                    right.append(x)
            return quick_sort(left) + middle + quick_sort(right)
            # Convert strings to lists of characters
        sorted_s = quick_sort(list(s))
        sorted_t = quick_sort(list(t))
        return sorted_s == sorted_t