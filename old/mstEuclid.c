#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct dynarray {
    int** data;
    int size;
    int capacity;
};
struct dynarray* dynarray_create() {
    struct dynarray* sp;
    sp = malloc(1000 * sizeof(struct dynarray));
    sp->data = malloc(1000 * sizeof(sp->data));
    sp->capacity = 2;
    sp->size = 0;
    return sp;
}
void dynarray_free(struct dynarray* da) {
    if (da != NULL)
    {
        free(da->data);
        free(da);
    }
    return;
}
void dynarray_insert(struct dynarray* da, void* val) {
    if (da->size >= da->capacity)
    {
        da->data = realloc(da->data, (da->capacity) * 100 * sizeof(da->data));
        da->capacity = 2 * da->capacity;
    }
    da->data[da->size] = val;
    da->size++;
    return;
}

void mst(int t, struct dynarray* array_1, struct dynarray* array_2) {

    int k[100][100];
    int point[100][2];
    int tmp = 1000;
    int tmp2 = 0;
    int a_tmp[2];
    int count = 0;
    int n = 0;
    int n_row = 0;
    int l = 0;
    int fd =0;

    for (int i = 0; i < t; i++) {    //put data into array
        point[i][0] = array_1->data[n];
        n++;
        point[i][1] = array_1->data[n];
        n++;
    }
    printf("Edges in MST\n");
    printf("Point (x,y)\t\tDistance\n");
    struct dynarray* cum;
    cum = dynarray_create();
    dynarray_insert(cum, 0);
    for (int j = 1; j < t; j++) {
        tmp = 100;
        for (int i = 0; i < t; i++) {
            if (i == l || k[l][i] == -1) {
                k[l][i] = -1;
            }
            else {
                k[l][i] = pow(pow(point[l][0] - point[i][0], 2) + pow(point[l][1] - point[i][1], 2), 0.5);

                for (int k1 = 0; k1 < j;k1++) {
                    if (i ==cum->data[k1]) {
                        k[l][i] = -1;
                        k[i][l] = -1;
                    }
                }
            }
        }
            count = 0 ;
            for (int n = 0; n < j; n++) { //find all points we already pass by
                tmp2 = cum->data[count];
                count++;
                for (int n1 =0 ; n1 < t ;n1++)
                {
                    if (k[tmp2][n1] <= tmp && k[tmp2][n1] != -1)
                    {
                        tmp = k[tmp2][n1];
                        a_tmp[0] = tmp2;
                        a_tmp[1] = n1;
                        n_row = n1;
                    }
                }
            }
        printf(" (%d,%d) - (%d,%d)   \t%d\n",point[a_tmp[0]][0],point[a_tmp[0]][1],point[a_tmp[1]][0], point[a_tmp[1]][1],tmp);
        dynarray_insert(cum,n_row);
        fd += tmp;

        k[a_tmp[0]][a_tmp[1]] = -1;
        k[a_tmp[1]][a_tmp[0]] = -1;

        l = a_tmp[1];
    }
    printf("final distance:\t%d", fd);
    return;
}

int main() {
    FILE* data = fopen("graph.txt", "r");
    if (data == NULL) {
        printf("Fail to open file");
        return 0;
    }
    char buffer[10];
    char* input = 0;
    size_t cur_len = 0;
    struct dynarray* array_1;
    struct dynarray* array_2;
    while (fgets(buffer, sizeof(buffer), data) != 0)//put data into input
    {
        size_t buf_len = strlen(buffer);
        char* extra = realloc(input, buf_len + cur_len + 1);
        if (extra == 0)
            break;
        input = extra;
        strcpy(input + cur_len, buffer);
        cur_len += buf_len;
    }
    array_1 = dynarray_create();
    array_2 = dynarray_create();
    int n = 0;
    char* T = strtok(input, "\r\n"); //first number
    int t = atoi(T);
    int tmp2 = 0;
    fclose(data);
    char* tmp = NULL;

    for (int i = 0; i < t; i++) {

            tmp = strtok(NULL, " ");
            tmp2 = atoi(tmp);
            dynarray_insert(array_1, tmp2);

            tmp = strtok(NULL, "\r\n");
            tmp2 = atoi(tmp);
            dynarray_insert(array_1, tmp2);
    }
    mst(t, array_1, array_2);

    /*
 *     data = fopen("results.txt", "w"); //write the data to txt
 *         int an = 1;
 *             while (an < array_2->size) {
 *                     if (array2->data[an] == "\r\n") {
 *                                 fputs(array_2->data[an], data);
 *                                             an++;
 *                                                     }
 *                                                             else {
 *                                                                         fputs(array_2->data[an], data);
 *                                                                                     fputs(" ", data);
 *                                                                                             }
 *                                                                                                     an++;
 *                                                                                                         }
 *
 *                                                                                                             fclose(data);
 *                                                                                                                 */

    free(input);
    return 0;
}
