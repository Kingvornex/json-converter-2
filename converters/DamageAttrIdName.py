def get_english_name(entry):
    if isinstance(entry.get("Names"), dict):
        name = entry["Names"].get("en")
        if name:
            return name

    if isinstance(entry.get("LinkedSkillTableNames"), dict):
        name = entry["LinkedSkillTableNames"].get("en")
        if name:
            return name

    if isinstance(entry.get("LinkedBuffNames"), dict):
        name = entry["LinkedBuffNames"].get("en")
        if name:
            return name

    if entry.get("Name"):
        return entry["Name"]

    return str(entry.get("Id", ""))


def convert(data):
    output = {}

    for key, value in data.items():
        output[str(key)] = get_english_name(value)

    return output
