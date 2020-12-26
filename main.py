def solution(lt=list):
    answer=False
    element=lt[0]
    lst=lt[1::]
    for i in lst:
        if element<=i:
            answer=True
        else:
            answer=False
            break
        element=i

    if answer:
        return answer
    else:
        x=False
        element=lt[0]
        for i in lst:
            if element>=i:
                answer=True
            else:
                answer=False
                break
            element=i
        if answer:
            return answer
        else: return  answer

def solution(a=list):
    n=0
    mis=0
    for i in a:
        n+=1
    lt=[i for i in range(n+1)]
    for i in lt:
        if i not in a:
            mis=i
    return mis
