def get_scene_name(entry):
    # Preferred: English translation
    if isinstance(entry.get("Names"), dict):
        if entry["Names"].get("en"):
            return entry["Names"]["en"]

        # Fallback: Simplified Chinese
        if entry["Names"].get("zh-CN"):
            return entry["Names"]["zh-CN"]

    # Fallback: Name field
    if entry.get("Name"):
        return entry["Name"]

    # Last resort
    return str(entry.get("Id", ""))


def convert(data):
    output = {}

    for key, value in data.items():
        output[str(key)] = get_scene_name(value)

    return output
