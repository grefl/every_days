import time

def bench(compute, count =  10):
    print('----------------------------------------------------------')
    print('----------------------BENCHMARKING------------------------')
    print('----------------------------------------------------------')
    for i in range(count):
        st = time.monotonic()
        compute()
        et = time.monotonic() - st
        print(f"{et* 1000:.2f}: ms {(et/1000)* 1000}: seconds")
