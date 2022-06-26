import yaml

def yaml_dump(file, data):
    with open(file, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

if __name__ == "__main__":
    filepath1 = "file.yaml"
    data1 = {
        "gadgets": {
            "monitor": 24,
            "laptop": 16,
            "mouse": "logitech"
        },
        "NamesAndAge": {
            "elon musk": 41,
            "shravan kamble": 19,
            "kunal kushwaha": 21
        }
    }
yaml_dump(filepath1, data1)
