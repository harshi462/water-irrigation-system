#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include <stdbool.h>

#define MAX_NODES 100

typedef struct Field {
    int id;
    int soilMoistureLevel; // 0-100
    int irrigationStatus;  // 0 (off) or 1 (on)
} Field;

// Global variables for MST
int graph[MAX_NODES][MAX_NODES];
int parent[MAX_NODES];
int key[MAX_NODES];
bool mstSet[MAX_NODES];
int V; // Number of fields/nodes

// Function declarations
void getUserInput(Field* fields, int numFields);
int simulateWeatherForecast();
void automateIrrigation(Field* fields, int numFields, int weatherForecast);
void monitorFields(Field* fields, int numFields);
int minKey();
void primMST();

int main() {
    srand((unsigned int)time(NULL)); // Seed random number generator

    printf("Enter the number of fields (max %d): ", MAX_NODES);
    if (scanf("%d", &V) != 1 || V <= 0 || V > MAX_NODES) {
        printf("Invalid number of fields.\n");
        return 1;
    }

    // Allocate memory for fields
    Field* fields = (Field*)malloc(V * sizeof(Field));
    if (fields == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    getUserInput(fields, V);

    // Simulate weather forecast
    int weatherForecast = simulateWeatherForecast();
    printf("\nWeather forecast: %s\n\n", weatherForecast ? "Rainy" : "Sunny");

    // Automate irrigation
    automateIrrigation(fields, V, weatherForecast);

    // Monitor fields
    printf("\nField Monitoring:\n");
    monitorFields(fields, V);

    // Initialize adjacency matrix for MST
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            graph[i][j] = 0;

    // Input edges for MST graph
    int edges;
    printf("\nEnter number of connections/edges between fields: ");
    scanf("%d", &edges);
    printf("Enter each connection as: from to weight\n");
    for (int i = 0; i < edges; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        graph[u][v] = w;
        graph[v][u] = w;
    }

    // Generate and display MST
    printf("\nMinimum Spanning Tree (Prim's Algorithm):\n");
    primMST();

    free(fields);
    return 0;
}

void getUserInput(Field* fields, int numFields) {
    for (int i = 0; i < numFields; i++) {
        fields[i].id = i;
        fields[i].soilMoistureLevel = rand() % 101;  // 0 to 100
        fields[i].irrigationStatus = 0;
    }
}

int simulateWeatherForecast() {
    return rand() % 2; // 0 for Sunny, 1 for Rainy
}

void automateIrrigation(Field* fields, int numFields, int weatherForecast) {
    for (int i = 0; i < numFields; i++) {
        if (weatherForecast == 0 && fields[i].soilMoistureLevel < 50) {
            fields[i].irrigationStatus = 1;
        } else {
            fields[i].irrigationStatus = 0;
        }
    }
}

void monitorFields(Field* fields, int numFields) {
    for (int i = 0; i < numFields; i++) {
        printf("Field %d -> Soil Moisture: %d, Irrigation: %s\n",
               fields[i].id,
               fields[i].soilMoistureLevel,
               fields[i].irrigationStatus ? "On" : "Off");
    }
}

int minKey() {
    int min = INT_MAX, min_index;

    for (int v = 0; v < V; v++) {
        if (!mstSet[v] && key[v] < min) {
            min = key[v], min_index = v;
        }
    }

    return min_index;
}

void primMST() {
    for (int i = 0; i < V; i++) {
        key[i] = INT_MAX;
        mstSet[i] = false;
    }

    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < V - 1; count++) {
        int u = minKey();
        mstSet[u] = true;

        for (int v = 0; v < V; v++) {
            if (graph[u][v] && !mstSet[v] && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    for (int i = 1; i < V; i++) {
        printf("%d - %d \tWeight: %d\n", parent[i], i, graph[i][parent[i]]);
    }
}
