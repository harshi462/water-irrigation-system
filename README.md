# water-irrigation-system
Prim's Minimum Spanning Tree (MST) Algorithm:
The primMST() function implements Prim's algorithm.
Purpose: To find the minimum-cost set of connections (edges) that connect all the fields together. This could be useful for minimizing the cost of laying out pipes or connecting control wires in the irrigation system.

Irrigation Automation Logic:
The automate Irrigation()function implements a simple set of rules to control irrigation:
If soil moisture is below a threshold AND it's sunny, turn irrigation ON.
If soil moisture is below a lower threshold AND it's rainy, turn irrigation ON.
Otherwise, turn irrigation OFF.

Weather Simulation:
The simulate Weather Forecast() function uses rand() % 2 to generate a random "weather forecast" (0 for sunny, 1 for rainy).
This is a very simple simulation for testing purposes. Real-world systems would likely integrate with actual weather forecast data.

Input Validation:
The getUserInput() function includes input validation to ensure that the user enters valid soil moisture levels (0-100).
The main() function also has input validation for the number of fields and the edges of graph.
Input validation is important for making the program more robust.

Arrays for Prim's Algorithm (parent, key, mstSet)
int parent[MAX_NODES];
int key[MAX_NODES];
bool mstSet[MAX_NODES];
