class Solution:
    def sortSentence(self, s: str) -> str:
        #create an empty string that will become the ordered sentense
        orderd_sentence=""
        #split each elemments of array s so they can be iterated 
        new_list=s.split()
        #create an outer loop so the the program continues for all the elements of array s
        for i in range(1,len(s)+1):
            #create an inner loop so that the program can compare each letter in every word
            for j in new_list:
                #compare if the value of the number at the end of the word is the same as the index number 
                if int(j[-1])==i:
                    #then update orderd sntense and subtract the last Number after the word
                    orderd_sentence+=j[:-1]
                    #after that  create a space
                    orderd_sentence+=" "
        #before returning he final sentense make sure to delete the last space after the last word            
        return orderd_sentence[:-1]
                    
            