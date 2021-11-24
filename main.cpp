// Jesús Palomino Hurtado (A01638492) - Ingenieria en Tecnologias Computacionales (ITC)
// Porfesor: Gildardo Sánchez Ante
// Instituto Tecnologico de Monterrey

// Objetivo del programa
// Enconctrar el camino hamiltoniano más corto dentro de un grafo por medio de la implementación de la tecnica Simulated Annealing

#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>

using namespace std;

void printGraph(vector<vector<int> > &graph)
{
    for (int i = 0; i < graph.size(); i++)
    {
        for (int j = 0; j < graph[0].size(); j++)
        {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}

// Function that reads x and y coordinates from txt file
vector<vector<float> > readCoordinates(string fileName)
{
    fstream file;
    // Opens an existing csv file or creates a new file.
    file.open(fileName, ios::in);
    // Error opening file
    if (file.fail())
    {
        cout << "Archivo " << fileName << " no fue posible de abrir" << endl;
    }
    vector<vector<float> > coordinates;
    vector<float> nodeCoordinates;
    float value;
    while (file.good())
    {
        nodeCoordinates.clear();
        file >> value;
        if (file.eof())
        {
            break;
        }
        nodeCoordinates.push_back(value);
        file >> value;
        nodeCoordinates.push_back(value);
        coordinates.push_back(nodeCoordinates);
    }
    return coordinates;
}

// Function that reads csv file passed as parameter and returns it's content in a format of a matrix made out of vectors
vector<vector<int> > readFile(string fileName)
{
    fstream file;
    // Opens an existing csv file or creates a new file.
    file.open(fileName, ios::in);
    // Error opening file
    if (file.fail())
    {
        cout << "Archivo " << fileName << " no fue posible de abrir" << endl;
    }
    vector<vector<int> > graph;
    vector<int> nodeRow;
    int pathValue;
    string line, stringValue;

    // Read line by line
    while (file >> line)
    {
        nodeRow.clear();

        stringstream s(line);
        // Separate each value in line
        while (getline(s, stringValue, ','))
        {
            pathValue = stoi(stringValue);
            nodeRow.push_back(pathValue);
        }
        graph.push_back(nodeRow);
    }
    return graph;
}

int main()
{
    vector<vector<int> > graph = readFile("cities_128.csv");
    vector<vector<float> > coordinates = readCoordinates("coordinates.txt");
    return 0;
}
