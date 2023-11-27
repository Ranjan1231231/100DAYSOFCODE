import sys
def solution(string):
    size=len(string)
    head=0
    tail=0
    chars=dict()
    max_len=1
    #starting index of the resultant substring
    s=0
    #ending index of the resultant substring
    e=0
    
    for tail in range(size):
        if string[tail] in chars:
            #current tail character already present inside hashmap
            if chars[string[tail]]>=head:
                head=chars[string[tail]]+1
        chars[string[tail]]=max(chars.get(string[tail],0),tail)
        if max_len<(tail-head+1):
            s=head
            e=tail
            max_len=e-s+1
    result_string=string[s:e+1]
    return result_string
string=str(input())
print(solution(string))
