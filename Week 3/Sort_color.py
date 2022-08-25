def Sort_color(nums):
    #0 means red
    #1 means White 
    #2 means blue
    #for this problem i we want to sort same colors together
    ##For This particular problem i used selection sort
    ##############Steps#################
    # 1. use and indexing variable to iterate through all the arry elemnts
    for i in range(1,len(nums)):
        # 2. in insertion sorting the arry will have a sorted and unsorted version.
        # 3. each time the i-1th elemnt is greater than the ith element we make a swap
        # 4. and since python uses negative index we limit our code to i>0
        while nums[i-1]>nums[i] and i>0:
            nums[i-1],nums[i]=nums[i],nums[i-1]
            # if there are any elments left that are greater than i we need to swap so we continue
            i-=1
    print(nums)

nums=[2,0,2,1,1,0]

Sort_color(nums)


