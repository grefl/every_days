#include <stdio.h>

int len(char s[]);
int len(char s[]) {
  int i = 0;
  while (s[i] != '\0')
    i += 1;
  return i;
}
void reverse(char s[]);
void reverse(char s[]) {
  int length = len(s);
  for (int i = 0; i < (length / 2); i +=1) {
    int other = length - i - 1;

    int temp = s[i];
    s[i] = s[other];
    s[other] = temp;
  }
}

int main() {
  char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
  reverse(greeting);
  printf("%s\n", greeting);
  return 0;
}

