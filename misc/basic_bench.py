import time

def bench(compute, count =  1000):
    print('----------------------------------------------------------')
    print('----------------------BENCHMARKING------------------------')
    print('----------------------------------------------------------')
    st = time.monotonic()
    for i in range(count):
        compute()
    et = time.monotonic() - st
    print(f"{et* 1000:.2f}: ms {(et/1000)* 1000}: seconds")
