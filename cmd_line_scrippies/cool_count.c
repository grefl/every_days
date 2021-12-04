#include <stdio.h>


int main() {
  int nwhitespace = 0;
  int nother = 0;
  int c,i;
  int ndigits[10];
  int nlower[26];
  int nhigher[26];
  
  for (i = 0; i  < 10; i +=1)
    ndigits[i] = 0;
  for (i = 0; i < 26; i +=1) {
    nhigher[i] = 0;
    nlower[i]  = 0;
  }


  while ((c = getchar()) != EOF)
    if (c >= '0' && c <= '9')
      ndigits[c-'0'] +=1;
    else if (c>= 'a' && c <='z')
      nlower[c-'a'] +=1;
    else if (c>= 'A' && c <='Z')
      nhigher[c-'A'] +=1;
    else if (c == ' ' || c == '\n' || c == '\t')
      nwhitespace +=1;
  for (i = 0; i < 10; i +=1)
    printf(" %d", ndigits[i]);
  printf("\n");
  for (i = 0; i < 26; i +=1) {
    printf(" %d", nlower[i]);
  }
  printf("\n");
  for (i = 0; i < 26; i +=1) {
    printf(" %d",nhigher[i]);
  }
  printf("\n");
  printf("white space = %d\n", nwhitespace);

    
  return 0;
}
