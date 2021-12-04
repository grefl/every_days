import sys
IN  = 1
OUT = 0 

def main():
    input = sys.argv[1] 
    lc = 0
    wc = 0
    cc = 0
    i  = 0
    state = OUT 
    while i < len(input):
        cc +=1
        char = input[i]
        if char == '\n':
            lc +=1
        if char == ' ' or char == '\n' or char == '\t':
           state = OUT
        elif state == OUT:
            wc +=1
            state = IN
        i += 1
    print(f"lc {lc} wc {wc} cc {cc}")
   

if __name__ == '__main__':
    main()
