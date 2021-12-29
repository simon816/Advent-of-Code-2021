#include "stdio.h"
#include "stdlib.h"

struct list_node {
    void *data;
    struct list_node *next;
};

struct list_node *ordered = NULL;

struct line {
    int x1, y1, x2, y2;
};

int min(int a, int b) { return a > b ? b : a; }
int max(int a, int b) { return a < b ? b : a; }

int main(int argc, char *argv[]) {
    int x1, y1, x2, y2;
    while(scanf("%d,%d -> %d,%d\n", &x1, &y1, &x2, &y2) == 4) {
        if (x2 < x1) {
            int tmp;
            tmp = x1;
            x1 = x2;
            x2 = tmp;
            tmp = y1;
            y1 = y2;
            y2 = tmp;
        }
        if (x1 != x2 && y1 != y2) {
            continue;
        }
        struct line *this_line = malloc(sizeof(struct line));
        this_line->x1 = x1;
        this_line->y1 = y1;
        this_line->x2 = x2;
        this_line->y2 = y2;
        struct list_node *this_node = malloc(sizeof(struct list_node));
        this_node->data = this_line;
        this_node->next = NULL;
        struct list_node *node = ordered;
        if (!node || ((struct line *)(node->data))->x1 > x1 ) {
            this_node->next = node;
            ordered = this_node;
            continue;
        }
        while(node->next) {
            struct line *line = node->next->data;
            if (line->x1 < x1) {
                node = node->next;
            } else {
                break;
            }
        }
        if (!node) {
            this_node->next = ordered;
            ordered = this_node;
        } else if (!node->next) {
            node->next = this_node;
        } else {
            this_node->next = node->next;
            node->next = this_node;
        }
    }
    int out = 0;
    struct list_node **traces = calloc(1000, sizeof(struct list_node *));
    for (int x = 0; x < 1000; x++) {
        while(ordered && ((struct line *) (ordered->data))->x1 == x) {
            struct list_node *curr = ordered;
            struct line *on_line = ordered->data;
            ordered = ordered->next;
            for (int y = min(on_line->y1, on_line->y2); y <= max(on_line->y1, on_line->y2); y++) {
                struct list_node *node = malloc(sizeof(struct list_node));
                int *ptr = malloc(sizeof(int));
                node->data = ptr;
                *ptr = on_line->x2;
                node->next = NULL;
                struct list_node *curr = traces[y];
                if (!curr) {
                    traces[y] = node;
                } else {
                    while(curr->next) curr = curr->next;
                    curr->next = node;
                }
            }
            free(curr->data);
            free(curr);
        }
        for (int y = 0; y < 1000; y++) {
            int active_count = 0;
            struct list_node *n = traces[y];
            struct list_node *new = NULL;
            struct list_node *new_prev = NULL;
            while(n) {
                active_count++;
                struct list_node *next_n = n->next;
                if (*((int *) (n->data)) > x) {
                    if (!new) new = n;
                    else new_prev->next = n;
                    new_prev = n;
                } else {
                    free(n->data);
                    free(n);
                }
                n = next_n;
            }
            if(new_prev) new_prev->next = NULL;
            traces[y] = new;
            if (active_count > 1) {
                out += 1;
            }
        }
    }
    free(traces);
    printf("%d\n", out);
    return 0;
}
