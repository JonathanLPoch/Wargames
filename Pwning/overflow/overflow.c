#include <unistd.h>
#include <stdio.h>

int main() {
    char the_buf[64];
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    printf("Oh look, your buffer is at: %p\n", the_buf);
    read(0, the_buf, 1024);

    printf("Ok, bye bye now!\n");
    return 0;
}
