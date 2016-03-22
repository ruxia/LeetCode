def towerHanoi(n,a,b,c):
    if n==1:
        print(a,'->',c)
    else:
        towerHanoi(n-1,a,c,b)
        towerHanoi(1,a,b,c)
        towerHanoi(n-1,b,a,c)

if __name__ == '__main__':
    towerHanoi(4,'a','b','c')
