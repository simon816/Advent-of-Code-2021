import sys

print("""
#include <stdio.h>

int w, x, y, z, IN[14];

void run() {
""")

inpos = 0
for line in sys.stdin.readlines():
    op, *args = line.strip().split(' ')
    args = tuple(args)
    if op == 'inp':
        invar = args[0]
        print("%s = IN[%d];" % (invar, inpos))
        inpos += 1
    elif op == 'add':
        print("%s += %s;" % args)
    elif op == 'mul':
        print("%s *= %s;" % args)
    elif op == 'div':
        print("%s /= %s;" % args)
    elif op == 'mod':
        print("%s %%= %s;" % args)
    elif op == 'eql':
        print("%s = %s == %s ? 1 : 0;" % (args[0], args[0], args[1]))

print("""
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
            printf("\\n");
            break;
        }
        if (IN[13] == 1) {
            for (int i = 13; i >= 0; i--) {
                if (i == 4) {
                    printf("Progress: ");
                    for (int i = 0; i < 14; i++) {
                        printf("%d", IN[i]);
                    }
                    printf("\\n");
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
""")
