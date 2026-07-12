def convert(data):
    result = {}

    for key, entry in data.items():
        # Use Id as output key if available, otherwise keep the original key
        output_key = str(entry.get("Id", key))

        result[output_key] = {
            "MonsterType": entry.get("MonsterType", 0),
            "Name": entry.get("Name", "")
        }

    return result
