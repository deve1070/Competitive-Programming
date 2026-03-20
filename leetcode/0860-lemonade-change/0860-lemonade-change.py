class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_counter=defaultdict(int)
        if bills[0] !=5:
            return False
        for bill in bills:
            if bill==5:
                bill_counter[5] +=1
                continue
            elif bill==10:
                bill_counter[10] +=1
                if bill_counter[5] >=1:
                    bill_counter[5]-=1
                else:
                    return False
            else:
                bill_counter[20]+=1
                if bill_counter[10]:
                    if bill_counter[5]:
                        bill_counter[10] -=1 
                        bill_counter[5]  -=1
                    else:
                        return False
                elif bill_counter[5] >=3:
                    bill_counter[5]-=3
                else:
                    return False
        return True

             

        