a=128
c=7
m=1000
seed = 27
def generate_random(a,c,m,k):
    x=seed
    ran=[]
    for i in range(k):
        x=(a*x+c)%m
        ran.append(x/m)
    return ran
   
def ks_test(ran):
    sorted_ran = sorted(ran)
    N = len(ran)
    d_plus=max([sorted_ran[i]-i/N for i in range(N)])
    d_minus=max([sorted_ran[i]-(i-1)/N for i in range(N)])  
    d=max(d_plus,d_minus)
    return d
   
def chi_square(ran,N):
    value = 0
    for i in range(N):
        no_of_no=0
        for no in ran:
            if(i/N<no<(i+1)/N):
                no_of_no+=1
        value += (len(ran)/N-no_of_no)**2/(len(ran)/N)
    return value
   
def runs(ran):
    runarray = []
    for i in range(len(ran)-1):
        if(ran[i]>ran[i+1]):
            runarray.append(0)
        else:
            runarray.append(1)
    runs_count=0
    for i in range(len(runarray)-1):
        if(runarray[i]!=runarray[i+1]):
            runs_count+=1
    n1=runarray.count(0)
    n2=runarray.count(1)
    mean = 2*(n1*n2)/(n1+n2) +1
    dev = ((mean-1)*(mean-2)/(n1+n2-1))**0.5
    d = (mean-runs_count)/dev
    return d
   
k=500
ran = generate_random(a,c,m,k)
print(ran)
print(ks_test(ran))
print(chi_square(ran,10))
print(runs(ran))
