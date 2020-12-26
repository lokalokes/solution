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
