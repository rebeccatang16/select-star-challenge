import json
import sys

if __name__ == "__main__":
    with open(sys.argv[1], "r") as json_file:
        data = json.load(json_file)
    
    fixturized_data = []
    word_pk = 0
    for i, prefix in enumerate(data):
        fixturized_prefix = {
            "model": "folder_view.Prefix",
            "pk": str(i + 1),
            "fields": {
                "name": prefix
            }
        }
        fixturized_data.append(fixturized_prefix)
  
        for word in data[prefix]: 
            word_pk += 1
            fixturized_word = {
                "model": "folder_view.Word",
                "pk": str(word_pk),
                "fields": {
                    "word": word,
                    "prefix": prefix
                }
            } 
            fixturized_data.append(fixturized_word)
    
    with open("fixture_data.json", "w") as fixture_file:
        json.dump(fixturized_data, fixture_file)
