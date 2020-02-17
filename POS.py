def POS(self, RGB, fps):
    l = int(fps)
    N = len(RGB)
    H = np.zeros(N)
    Pp = np.array([[0,1,-1], [-2,1,1]])
    for n in range(0, N):       
        m = n - l
        if m > 0:
            Cmn = RGB[m:n, :].T
            Cn = (Cmn / np.average(Cmn))
            S = np.matmul(Pp, Cn)
            S1 = S[0,:]
            S2 = S[1,:]
            h = S1 + (np.std(S1)/np.std(S2))*S2
            H[m:n] = H[m:n] + (h - np.average(h))
    return H
