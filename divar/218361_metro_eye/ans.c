#include <stdio.h>
#include <string.h>

int main() {
    char r1[9], r2[9];
    int count = 0;

    scanf("%s", r1);

    scanf("%s", r2);
    for(int i = 0; i < 8; i++) {
        if(r1[i] == '1' && r2[i] == '1') {
            count++;
        }
    }

    printf( count);

    return 0;
}
