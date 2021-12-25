
#include <stdio.h>

int w, x, y, z, IN[14];

void run() {
w = IN[0];
z = (w + 6);
w = IN[1];
z = ((z * 26) + (w + 11));
w = IN[2];
z = ((z * 26) + (w + 5));
w = IN[3];
z = ((z * 26) + (w + 6));
w = IN[4];
z = ((z * 26) + (w + 8));
w = IN[5];
x = (((z % 26) + -1) != w) ? 1 : 0;
z = (((z / 26) * ((25 * x) + 1)) + ((w + 14) * x));
w = IN[6];
z = ((z * 26) + (w + 9));
w = IN[7];
x = (((z % 26) + -16) != w) ? 1 : 0;
z = (((z / 26) * ((25 * x) + 1)) + ((w + 4) * x));
w = IN[8];
x = (((z % 26) + -8) != w) ? 1 : 0;
z = (((z / 26) * ((25 * x) + 1)) + ((w + 7) * x));
w = IN[9];
z = ((z * 26) + (w + 13));
w = IN[10];
x = (((z % 26) + -16) != w) ? 1 : 0;
z = (((z / 26) * ((25 * x) + 1)) + ((w + 11) * x));
w = IN[11];
x = (((z % 26) + -13) != w) ? 1 : 0;
z = (((z / 26) * ((25 * x) + 1)) + ((w + 11) * x));
w = IN[12];
x = (((z % 26) + -6) != w) ? 1 : 0;
z = (((z / 26) * ((25 * x) + 1)) + ((w + 6) * x));
w = IN[13];
x = (((z % 26) + -6) != w) ? 1 : 0;
z = (((z / 26) * ((25 * x) + 1)) + ((w + 1) * x));
}
int main(int argc, char *argv[]) {
    for (int i = 0; i < 14; i++) {
        IN[i] = 9;
    }
    IN[1] = 7;
    while (1) {
        w = x = y = z = 0;
        run();
        if (z == 0) {
            for (int i = 0; i < 14; i++) {
                printf("%d", IN[i]);
            }
            printf("\n");
            break;
        }
        if (IN[13] == 1) {
            for (int i = 13; i >= 0; i--) {
                if (i == 4) {
                    printf("Progress: ");
                    for (int i = 0; i < 14; i++) {
                        printf("%d", IN[i]);
                    }
                    printf("\n");
                }
                if (IN[i] == 1) {
                    IN[i] = 9;
                } else {
                    IN[i] -= 1;
                    break;
                }
            }
        } else {
            IN[13] -= 1;
        }
    }
    return 0;
}

