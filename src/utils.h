#include <rapidjson/document.h>
#include <rapidjson/pointer.h>
#include <string>
#include <fstream>

void read_json_file(std::string path, rapidjson::Document &res){
    //open file and jump to the end
    std::ifstream fs(path, std::ios::ate);
    size_t filesize = fs.tellg();
    std::string file_content;
    file_content.resize(filesize);
    //jump to beginning of file
    fs.seekg(0);
    fs.read(&file_content[0], filesize);
    res.ParseInsitu(&file_content[0]);
}