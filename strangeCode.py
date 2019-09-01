def strangeCode(s, e):
    ans = ""
    while (s < (e-1)):
        s+=1
        e-=1
        if (ans == ""):
            ans+="a"
        else:
            if (ans[-1]=="a"):
                ans+="b"
            else:
                ans+="a"
    return (ans)
