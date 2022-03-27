# You are given a string as input. You have to find the number of words that have unique characters in it(i.e. no single character is repeated) and length of the word must be greater than 3.
# 
def count_unique_words(inp):
    inp=inp.split(" ")
    count1=0
    final_ans=[]
    flag=False
    for i in range(len(inp)):
        a=inp[i]
        #print(a,len(a))
        if len(a)>3:
            ans=[]
            for j in range(len(a)):
                if j==0:ans.append(a[j])  
                elif a[j] not in ans:
                    ans.append(a[j])
                    flag=True
                else:
                    flag=False
                    ans=[]
                    break
                #print(ans,flag)
            if flag==True:
                final_ans.append(a)
        #print(final_ans)
    return len(final_ans)