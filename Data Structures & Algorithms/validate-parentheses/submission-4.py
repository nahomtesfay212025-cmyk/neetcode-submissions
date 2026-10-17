class Solution:
    def isValid(self, s: str) -> bool:
        """
        undertstand: 
        input: string
        output: bool

        plan:
        if length of string is odd lets return false
        if first item is on of the closing signs then return false too

        lets create a dict that maps closing with opening
        create empty list
        then iterate through the string and if item is one of the opening append it
        else compare the last item using the item as key to find  vlaue in the dict and if they not same return false

        out side loop return true


        """
        if len(s) == 0 or len(s) % 2 != 0:
            return False
        if s[0] in set("}])"):
            return False
        
        new_dict = {"}": "{", ")": "(", "]":"["}
        new_list = []
        for ch in s:
            if ch in set("{[("):
                new_list.append(ch)
            else:
                if not new_list:
                    return False
                else:
                    if new_list[-1] != new_dict[ch]:
                        return False
                    else:
                        new_list.pop()
            
        return len(new_list) == 0


