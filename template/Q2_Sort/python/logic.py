class Logic:
    # この中に解答を記述してください
    def sort(self, ARRAY, DIGITS): 
        try:
            array = []
            for num , element in enumerate(sorted(ARRAY)):
                count = ('{0:05d}'.format(element)) 
                array.append(count)

            rem_list, rem_1 = _sort_(array, DIGITS)
            rem_list1, rem_2 = _sort_(rem_1, DIGITS)
            rem_list2, rem_3 = _sort_(rem_2, DIGITS)
            rem_list3, rem_4 = _sort_(rem_3, DIGITS)
            rem_list4 = []
            rem_list5 = []
            for n in range(len(rem_4)):
                if int(rem_4[n][-DIGITS]) == 0:
                    rem_list4.append(int(rem_4[n]))
                else:
                    rem_list5.append(int(rem_4[n]))

            if DIGITS == 1: #桁が0で被った時のsort　+ 1で被った時sort + 2sort + 3sort + 4sort　+ 5sort
                result = rem_list4 + rem_list + rem_list1 + rem_list2 + rem_list3 + rem_list5
            if DIGITS == 2 or DIGITS == 3: #rem_lis5 は DIGITS = 2で使用
                result = rem_list + rem_list1 + rem_list5  + rem_list3 + rem_list2 
            if DIGITS == 4 or DIGITS == 5: #rem_lis2 は DIGITS = 4で使用
                result = rem_list + rem_list2 + rem_list1
                
            return result
        
        except (IndexError, UnboundLocalError, TypeError) :
            print(" １ から ５ の自然数を入力してください")
            import sys
            sys.exit()

def _sort_(list, digit): #桁の数字が同じ時、小さい桁順にsortする関数
    brank_list = []
    remainder_list = []
    for repeat in range(len(list)):
        if int(list[0][-digit]) == int(list[repeat][-digit]):        
            brank_list.append(int(list[repeat])) #同じ数字でsortされたlist
        else:
            remainder_list.append(list[repeat]) #同じ数字ではなくsortされなかったlist
    return brank_list, remainder_list
