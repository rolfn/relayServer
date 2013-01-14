
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

unsigned long long millisecondsSinceEpoch() {
  struct timeval t;
  gettimeofday(&t, NULL);
  return (unsigned long long)(t.tv_sec) * 1000 +
    (unsigned long long)(t.tv_usec) / 1000;
}

int	main(int argc, char *argv[]) {

  printf("%llu\n", millisecondsSinceEpoch());
  
	return 0;
}

