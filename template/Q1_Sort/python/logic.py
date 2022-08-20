class Logic:
    # この中に解答を記述してください
    def sort(self, ARRAY): #lay:層, sp:分解, ele:要素
        array_ant = fanc(ARRAY[:5])
        array_post = fanc(ARRAY[5:])
        for num in range(len(array_post)):
            array_ant.append(array_post[num])
        result = sorted(array_ant)
        return result

def fanc(_array_): #分解-結合_sort
    lay2_sp2 = _array_[3:] #2個
    lay345 = split1_bind2(lay2_sp2) 

    lay2_sp3 = _array_[:3] 
    lay3_sp2 = lay2_sp3[:2]
    lay456 = split1_bind2(lay3_sp2)

    lay3_ele = lay2_sp3[2:] #1個
    lay456.append(*lay3_ele) 
    final_lay = sorted(lay456) #1+2個_sort

    for n in range(len(lay345)): 
        final_lay.append(lay345[n]) 
    final_lay.sort() #3+2個_sort
    return final_lay

def split1_bind2(lay_sp): #1+1個_sort
    bind = []
    bind.append(*lay_sp[:1])
    bind.append(*lay_sp[1:])
    bind = sorted(bind)
    return bind
