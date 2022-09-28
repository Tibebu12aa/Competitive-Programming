class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last_fruit=-1
        sec_last_fruit=-1
        last_fruit_count=0
        current_max=0
        Max=0
        for fruit in fruits:
            if fruit==last_fruit or fruit==sec_last_fruit:
                current_max+=1
            else:
                current_max=last_fruit_count+1
            
            if fruit==last_fruit:
                last_fruit_count+=1
            else:
                last_fruit_count=1
            
            if fruit!=last_fruit:
                sec_last_fruit=last_fruit
                last_fruit=fruit
            
            
            Max=max(current_max,Max)
        return Max