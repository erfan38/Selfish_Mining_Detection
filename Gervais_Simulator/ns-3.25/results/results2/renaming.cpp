/*#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>

int main() {
    const std::string baseName = "benign_eachnode";
    const std::string extension = ".csv";
    const int numFiles = 124;

    for (int i = 1; i <= numFiles; ++i) {
        std::string oldName = baseName + std::to_string(i) + extension;
        std::string newName = baseName + std::to_string(i) + extension;

        if (std::rename(oldName.c_str(), newName.c_str()) == 0) {
            std::cout << "Renamed " << oldName << " to " << newName << std::endl;
        } else {
            std::cerr << "Error renaming " << oldName << std::endl;
        }
    }

    return 0;
}
*/

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <sstream> // For stringstream

int main() {
    const std::string baseName = "benign_eachnode";
    const std::string extension = ".csv";
    const int numFiles = 124;

    for (int i = 1; i <= numFiles; ++i) {
        std::string oldName = baseName + std::to_string(i) + extension;
        std::string newName = baseName + std::to_string(i) + extension;

        std::stringstream newNameStream;
        newNameStream << baseName << i << extension;
        newName = newNameStream.str();

        if (std::rename(oldName.c_str(), newName.c_str()) == 0) {
            std::cout << "Renamed " << oldName << " to " << newName << std::endl;
        } else {
            std::cerr << "Error renaming " << oldName << std::endl;
        }
    }

    return 0;
}

