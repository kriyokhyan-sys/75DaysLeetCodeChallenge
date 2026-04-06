#include <stdlib.h>
#include <math.h>

long long get_key(int x, int y) {
    return ((long long)(x + 30000) << 32) | (long long)(y + 30000);
}

int compare(const void* a, const void* b) {
    long long arg1 = *(const long long*)a;
    long long arg2 = *(const long long*)b;
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int robotSim(int* commands, int commandsSize, int** obstacles, int obstaclesSize, int* obstaclesColSize) {
    int dx[] = {0, 1, 0, -1};
    int dy[] = {1, 0, -1, 0};
    int x = 0, y = 0, di = 0;

    long long* obstacleKeys = (long long*)malloc(obstaclesSize * sizeof(long long));
    for (int i = 0; i < obstaclesSize; i++) {
        obstacleKeys[i] = get_key(obstacles[i][0], obstacles[i][1]);
    }
    qsort(obstacleKeys, obstaclesSize, sizeof(long long), compare);

    int maxDistSq = 0;

    for (int i = 0; i < commandsSize; i++) {
        if (commands[i] == -2) {
            di = (di + 3) % 4;
        } else if (commands[i] == -1) {
            di = (di + 1) % 4;
        } else {
            for (int k = 0; k < commands[i]; k++) {
                int nextX = x + dx[di];
                int nextY = y + dy[di];
                long long key = get_key(nextX, nextY);
                
                if (bsearch(&key, obstacleKeys, obstaclesSize, sizeof(long long), compare) == NULL) {
                    x = nextX;
                    y = nextY;
                    int currentDistSq = x * x + y * y;
                    if (currentDistSq > maxDistSq) {
                        maxDistSq = currentDistSq;
                    }
                } else {
                    break;
                }
            }
        }
    }

    free(obstacleKeys);
    return maxDistSq;
}