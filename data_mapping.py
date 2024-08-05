import json

# Function to map data to objects
def map_data_to_objects(object_paths, descriptions, texts, summaries):
    data = {}
    for object_id in object_paths.keys():
        data[object_id] = {
            "file_path": object_paths[object_id],
            "description": descriptions.get(object_id, "N/A"),
            "text": texts.get(object_id, "N/A"),
            "summary": summaries.get(object_id, "N/A")
        }
    return data


data = map_data_to_objects(object_paths, descriptions, texts, summaries)

# JSON file
with open('object_data.json', 'w') as f:
    json.dump(data, f, indent=4)
