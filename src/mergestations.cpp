#include <rapidjson/document.h>
#include <rapidjson/pointer.h>
#include <algorithm>
#include <ranges>
#include <map>
#include <fstream>
#include <string>
#include <iostream>
#include <vector>

inline void create_properties_paths(size_t feature_index, std::map<std::string, std::string> &desired_properties){
    for(auto& [property, path] : desired_properties){
        path = "/features/" + std::to_string(feature_index) + "/properties/" + property;
    }
}

void get_properties_values(size_t feature_index, std::map<std::string, std::string> &desired_properties, rapidjson::Document &dom){
    create_properties_paths(feature_index, desired_properties);
    for(auto&& [property, path] : desired_properties){
        //TODO: change type of map value to rapidjson::Value, to handle numbers as well as strings
        desired_properties[property] = rapidjson::Pointer(path.c_str()).Get(dom)->GetString();
    }
}

void set_properties_values(size_t feature_index, std::map<std::string, std::string> &desired_properties, rapidjson::Document &dom){
    create_properties_paths(feature_index, desired_properties);
    for(const auto& [property, path] : desired_properties){
        rapidjson::Pointer(path.c_str()).Set(dom, property.c_str());
    }
}

void get_relevant_betriebsstellen(rapidjson::Document & res){
    rapidjson::Document stellen;

    //setup result json document
    rapidjson::Pointer("/type").Set(res, "FeatureCollection");
    rapidjson::Pointer("/name").Set(res, "betriebsstellen_merged");

    read_json_file("geojson/betriebsstellen.geojson", stellen);
    assert(stellen.IsObject());
    assert(stellen.HasMember("features"));
    assert(stellen["features"].IsArray());
    std::vector<std::string> stellen_list;
    rapidjson::Document::Array stellen_feat = stellen["features"].GetArray();

    // number of operating sites already added to the result json document
    size_t count = 0;
    for(size_t i = 0; i < stellen_feat.Size(); i++){
        std::map<std::string, std::string> desired_properties = {{"art",""}, {"kuerzel",""}, {"km_i",""}};
        get_properties_values(i, desired_properties, stellen);
        
        // std::string art = stellen_feat[i]["properties"]["art"].GetString();
        // std::string kuerzel = stel["properties"]["kuerzel"].GetString();
        if(desired_properties["art"] != "üst" && desired_properties["art"] != "Bk" && std::find(stellen_list.begin(), stellen_list.end(), desired_properties["kuerzel"]) != stellen_list.end()){
            count++;
            set_properties_values(count, desired_properties, res);
        }
    }

}

void test(std::map<std::string, std::string> &test){
    test["test"] = "changed";
}
int main(){
    rapidjson::Document strecken;
    read_json_file("geojson/strecken.geojson", strecken);

    rapidjson::Document betriebsstellen;
    read_json_file("geojson/strecken.geojson", betriebsstellen);
    rapidjson::Document relevante_betriebsstellen;
    get_relevant_betriebsstellen(relevante_betriebsstellen);
}