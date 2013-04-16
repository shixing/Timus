#include <cstdio>

using namespace std;

const int N = 1000 * 1000;

char a[N];

int main(int argc, char const *argv[])
{
  int i, j, n, x, y;
  scanf("%d\n", &n);
  for (i = 0; i < n; i++) {
    scanf("%d %d\n", &x, &y);
    a[i] = x + y;
    for (j = i; a[j] > 9; j--) {
      a[j - 1]++;
      a[j] -= 10;
    }
  }
  for (i = 0; i < n; i++) printf("%d", a[i]);
  puts("");
  return 0;
}
