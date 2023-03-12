import json

def remove_irrelevant_info(filename):
    with open() as f:
        bsts = json.load(f)

    for bst in bsts:
        del bst["features"]["properties"]
        
def merge_stations(filename):
    with open(filename) as f:
        bsts = json.load(f)

    kuerzel = []
    counter = 0
    bsts_list_neu = []
    print(type(bsts["features"]))
    for bst in bsts["features"]:
        # print(bsts["features"])
        try:
            i = kuerzel.index(bst["properties"]["kuerzel"])
            bsts_list_neu[i]["properties"]["streckennu"].append(bst["properties"]["streckennu"][0])
            # print(kuerzel)
            # print(i)
            # print(f'adding {bst["properties"]["kuerzel"]} to {bsts_list_neu[i]["properties"]["kuerzel"]}')
            
        except ValueError:
            bst["properties"]["adj_nr"] = counter
            bsts_list_neu.append(bst)
            # print("new list: " + str(bsts_list_neu))
            kuerzel.append(bst["properties"]["kuerzel"])
            # print(f'appending {bst["properties"]["kuerzel"]} to list')
            counter += 1

    bsts["features"] = bsts_list_neu
    with open(filename+"_w", "w") as f:
        json.dump(bsts, f, ensure_ascii=False)

def convert_strnr_to_list(filename):
    with open(filename, "r") as f:
        bsts = json.load(f)
    for bst in bsts["features"]:
        bst["properties"]["streckennu"] = [bst["properties"]["streckennu"]]

    with open(filename+"_w", "w") as f:
        json.dump(bsts, f)

merge_stations("geojson/betriebsstellen_list.geojson")
# convert_strnr_to_list("geojson/bsts.geojson")