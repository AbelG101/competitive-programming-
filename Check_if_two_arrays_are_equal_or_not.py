    def check(self,A,B,N):
        
        a_dict = {}
        
        for num in A:
            if num in a_dict:
                a_dict[num] += 1
            else: a_dict[num] = 1
            
        for num in B:
            if num in a_dict and a_dict[num] > 0:
                a_dict[num] -= 1
            else: return False
            
        return True
