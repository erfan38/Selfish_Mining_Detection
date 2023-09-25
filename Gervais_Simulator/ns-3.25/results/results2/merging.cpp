#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

int main() {
    const int numFiles = 100;
    const std::string baseFilename = "benign_eachnode";
    const std::string outputFilename = "merged_output.csv";

    std::ofstream outputFile(outputFilename);
    if (!outputFile.is_open()) {
        std::cerr << "Unable to open output file for writing." << std::endl;
        return 1;
    }

    // Write header from the first file
    std::ifstream firstFile(baseFilename + "123455.csv");
    if (!firstFile.is_open()) {
        std::cerr << "Unable to open the first input file." << std::endl;
        return 1;
    }
    std::string header;
    std::getline(firstFile, header);
    outputFile << header << std::endl;
    firstFile.close();

    // Loop through and append data from each file
    for (int i = 1; i <= numFiles; ++i) {
        std::string filename = baseFilename + std::to_string(i) + ".csv";
        std::ifstream inputFile(filename);
        if (!inputFile.is_open()) {
            std::cerr << "Unable to open input file: " << filename << std::endl;
            return 1;
        }

        // Skip the header in subsequent files
        std::string line;
        std::getline(inputFile, line);

        // Append the data to the output file
        while (std::getline(inputFile, line)) {
            outputFile << line << std::endl;
        }

        inputFile.close();
    }

    outputFile.close();

    std::cout << "Merged " << numFiles << " CSV files into " << outputFilename << std::endl;

    return 0;
}

