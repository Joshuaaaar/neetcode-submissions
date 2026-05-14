class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #using a hash map
        d = Counter(nums)


        sorted_d = dict(sorted(d.items(),key=lambda x: x[1] , reverse=True))

       # print(sorted_d)

        final_lst = []
        i = 0
       

        for key in sorted_d.keys():
            
            if i == k:
                break
            final_lst.append(key)
            
            i+=1

        return final_lst







        # lst_to_return = []

        # lst_of_tuple = list(d.items())

        # print(lst_of_tuple)

        # i = 0 
        
        # final_lst = []

        # while i < k:

        #     final_lst.append(lst_of_tuple[i][0])

        #     i +=1
        
        # return final_lst










            

        




