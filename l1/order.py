def execute(filepath):
    with open(filepath) as f:
        lines = [line.rstrip('\n') for line in f]
        print(lines)
        n = 0
        m = 0
        second = False
        for x in lines:
            try:
                p = int(x)
            except Exception:
                p = "n"
            if isinstance(p, int):
                if n == 0:
                    y = []
                    for q in range(0,p):
                        y.append(q)
                else:
                    z = []
                    for q in range(0,p):
                        z.append(q)
                    second = True
            elif not isinstance(p,int) and n != 0:
                if not second:
                    temp = x.split()
                    y[n-1] = temp
                else:
                    temp = x.split()
                    z[m] = temp
            n = n + 1
        return y, z