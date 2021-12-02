#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

static size_t get_int(char *addr, size_t i, int len, int *value) {
    *value = 0;
    for (; i < len; i++) {
        if (addr[i] == 10) {
            i++;
            break;
        }
        *value *= 10;
        *value += addr[i] - 30;
    }
    return i;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        return 1;
    }
    int fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        return 1;
    }
    struct stat stat;
    if (fstat(fd, &stat) == -1) {
        goto file_clean;
    }
    int len = stat.st_size;
    char *addr = mmap(NULL, len, PROT_READ, MAP_PRIVATE, fd, 0);
    if (addr == MAP_FAILED) {
        goto file_clean;
    }

    int count = 0;
    size_t i = 0;
    int prev = 0x7fffffff;
    while (i < len) {
        int val;
        i = get_int(addr, i, len, &val);
        if (val > prev) {
            count++;
        }
        prev = val;
    }

    printf("%d\n", count);

    munmap(addr, len);

    file_clean:
    close(fd);

    return 0;
}
