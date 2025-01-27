def solution(polynomial):
    terms = polynomial.split(" + ")
    a, b = 0, 0
    for term in terms:
        if "x" in term:
            if term == "x":
                a += 1
            else:
                a += int(term[:-1])

        else:
            b += int(term)

    a_list= []
    if a > 0 :
        if a == 1:
            a_list.append("x")
        else:
            a_list.append(f"{a}x")
    if b > 0:
        a_list.append(str(b))

    answer = " + ".join(a_list)
    return answer