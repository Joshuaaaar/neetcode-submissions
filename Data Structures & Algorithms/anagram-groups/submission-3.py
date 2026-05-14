class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # edge case
        if len(strs) == 1:
            return [[strs[0]]]
        
        seen = set()

        for agn in strs:
            lst = sorted(agn)
            x = "".join(lst)
            if x not in seen:
                seen.add(x)
        
        final_lst = []

        for elem in seen:
            sub_lst = [] 

            for index in range(len(strs)):

                sorted_char = sorted(strs[index])

                combined_char = "".join(sorted_char)

                if elem == combined_char:
                    sub_lst.append(strs[index])
            
            final_lst.append(sub_lst)
            
        return final_lst



        #print(seen)

        #print(seen)


        # lst_of_d = []
        # for agn in strs:

        #     lst_of_d.append(Counter(strs))
        
        # print(lst_of_d)

    #     lst_of_sorted = []

    #     for agn in strs:
    #     #    print(agn)
    #         sort_a = sorted(agn)
    #    #     print(sort_a)
    #         lst_of_sorted.append(sort_a)
        
    #     i = 0 

    #     sub_lst = []

    #     for index in range(len(lst_of_sorted)):
            
    #         together_lst = []
    #         together_lst.append(strs[index])

    #         for index1 in range(index + 1  , len(lst_of_sorted)):

    #             if lst_of_sorted[index] == lst_of_sorted[index1]:
    #                 lst

        



            











        
      #  print(lst_of_sorted)


    

        








            


        


