#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC; //568134124 / 5 = 113626825
                       //0x06C5CEC9
//sums each set of 8 bits
unsigned long check_password(const char* p){
    int* ip = (int*)p;
    int i;
    int res=0;
    for(i=0; i<5; i++){
        printf("ip: %x\n", *ip);
        res += ip[i];
    }
    return res;
}


int main(int argc, char* argv[]){
    printf("%d\n", argc);
    if(argc<2){
        printf("usage : %s [passcode]\n", argv[0]);
        return 0;
    }
    printf("%lu\n", strlen(argv[1]));
    if(strlen(argv[1]) != 20){
        printf("passcode length should be 20 bytes\n");
        return 0;
    }
    printf("Hash: %x\n", check_password(argv[1]));
    if(hashcode == check_password( argv[1] )){
        return 0;
    }
    else
        printf("wrong passcode.\n");
    return 0;
}
// This is little endian
// ./col $(perl -e 'print "\xC9\xCE\xC5\x06" x 5') gives 0x21dd09ed, so + 1
// This should work...
// ./col $(perl -e 'print "\xC9\xCE\xC5\x06" x 4 . "\xc8\xCE\xC5\x06"')
