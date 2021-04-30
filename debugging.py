import pdb


def seq(n):
    for i in range(n):
        pdb.set_trace()  # breakpoint, c:continue q:quit h:help list p:print p locals() p globals() d:down etc
        print(i)
    return


seq(5)

