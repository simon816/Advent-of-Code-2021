
#include <stdio.h>

int w, x, y, z, IN[14];

void run() {

w = IN[0];
x *= 0;
x += z;
x %= 26;
z /= 1;
x += 13;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 6;
y *= x;
z += y;
w = IN[1];
x *= 0;
x += z;
x %= 26;
z /= 1;
x += 11;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 11;
y *= x;
z += y;
w = IN[2];
x *= 0;
x += z;
x %= 26;
z /= 1;
x += 12;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 5;
y *= x;
z += y;
w = IN[3];
x *= 0;
x += z;
x %= 26;
z /= 1;
x += 10;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 6;
y *= x;
z += y;
w = IN[4];
x *= 0;
x += z;
x %= 26;
z /= 1;
x += 14;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 8;
y *= x;
z += y;
w = IN[5];
x *= 0;
x += z;
x %= 26;
z /= 26;
x += -1;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 14;
y *= x;
z += y;
w = IN[6];
x *= 0;
x += z;
x %= 26;
z /= 1;
x += 14;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 9;
y *= x;
z += y;
w = IN[7];
x *= 0;
x += z;
x %= 26;
z /= 26;
x += -16;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 4;
y *= x;
z += y;
w = IN[8];
x *= 0;
x += z;
x %= 26;
z /= 26;
x += -8;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 7;
y *= x;
z += y;
w = IN[9];
x *= 0;
x += z;
x %= 26;
z /= 1;
x += 12;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 13;
y *= x;
z += y;
w = IN[10];
x *= 0;
x += z;
x %= 26;
z /= 26;
x += -16;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 11;
y *= x;
z += y;
w = IN[11];
x *= 0;
x += z;
x %= 26;
z /= 26;
x += -13;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 11;
y *= x;
z += y;
w = IN[12];
x *= 0;
x += z;
x %= 26;
z /= 26;
x += -6;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 6;
y *= x;
z += y;
w = IN[13];
x *= 0;
x += z;
x %= 26;
z /= 26;
x += -6;
x = x == w ? 1 : 0;
x = x == 0 ? 1 : 0;
y *= 0;
y += 25;
y *= x;
y += 1;
z *= y;
y *= 0;
y += w;
y += 1;
y *= x;
z += y;

}
int main(int argc, char *argv[]) {
    for (int i = 0; i < 14; i++) {
        IN[i] = 9;
    }
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

