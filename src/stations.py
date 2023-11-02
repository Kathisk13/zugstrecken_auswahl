import json

def remove_irrelevant_info(filename):
    with open() as f:
        bsts = json.load(f)

    for bst in bsts:
        del bst["features"]["properties"]
        
def merge_stations(filename):
    """
    Erstellt eine neue geojson Datei mit sämtlichen Betriebsstellen genau einmal.
    """
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
            bsts_list_neu[i]["properties"]["streckennu"].append(bst["properties"]["streckennu"])

            # print(kuerzel)
            # print(i)
            # print(f'adding {bst["properties"]["kuerzel"]} to {bsts_list_neu[i]["properties"]["kuerzel"]}')
            
        except ValueError:
            bsts_list_neu.append(bst)
            # print("new list: " + str(bsts_list_neu))
            kuerzel.append(bst["properties"]["kuerzel"])
            # print(f'appending {bst["properties"]["kuerzel"]} to list')
            counter += 1

    bsts["features"] = bsts_list_neu
    with open(filename+"_w", "w") as f:
        json.dump(bsts, f, ensure_ascii=False)

def make_graph(filename):
    with open(filename) as f:
        bsts = json.load(f)
    
    graph = {}
    dist1 = float("inf")
    dist2 = float("inf")
    temp1_bst = None
    temp2_bst = None
    for i,bst1 in enumerate(bsts["features"]):
        bst1_p = bst1["properties"]
        for bst2 in bsts["features"][i:]:
            bst2_p = bst2["properties"]
            if bst1_p["streckennu"] == bst2_p["streckennu"]:
                if bst1_p["km_i"] < bst2_p["km_i"] and bst2_p["km_i"] - bst1_p["km_i"] < dist1:
                    temp1_bst = bst2
                elif bst1_p["km_i"] > bst2_p["km_i"] and bst2_p["km_i"] - bst1_p["km_i"] < dist2:
                    temp2_bst = bst2
        if bst1_p["kuerzel"] in graph:
            if temp1_bst:
                graph[bst1_p["kuerzel"]].append(temp1_bst["properties"]["kuerzel"])
            if temp2_bst:
                graph[bst1_p["kuerzel"]].append(temp2_bst["properties"]["kuerzel"])
        else:
            if temp1_bst:
                graph[bst1_p["kuerzel"]] = [temp1_bst["properties"]["kuerzel"]]
            if temp2_bst:
                graph[bst1_p["kuerzel"]] = [temp2_bst["properties"]["kuerzel"]]

    with open("graph",'w') as f:
        json.dump(graph, f, ensure_ascii=False)


make_graph("geojson/betriebsstellen.geojson")
# merge_stations("geojson/betriebsstellen_list.geojson")
# convert_strnr_to_list("geojson/bsts.geojson")