def get_scene_name(entry):
    # 1. English translation
    names = entry.get("Names")
    if isinstance(names, dict):
        name = names.get("en")
        if name:
            return name

    # 2. Name
    name = entry.get("Name")
    if name:
        return name

    # 3. NameDesign
    name = entry.get("NameDesign")
    if name:
        return name

    # 4. Simplified Chinese
    if isinstance(names, dict):
        name = names.get("zh-CN")
        if name:
            return name

    # 5. NameId
    name_id = entry.get("NameId")
    if name_id is not None:
        return str(name_id)

    # 6. Id
    return str(entry.get("Id", ""))


def convert(data):
    output = {}

    for key, value in data.items():
        output[str(key)] = get_scene_name(value)

    return output
