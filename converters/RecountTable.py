def get_recount_name(entry):
    # Preferred: English translation
    if isinstance(entry.get("Names"), dict):
        name = entry["Names"].get("en")
        if name:
            return name

        # Fallback: Simplified Chinese
        name = entry["Names"].get("zh-CN")
        if name:
            return name

    # Fallback: RecountName field
    if entry.get("RecountName"):
        return entry["RecountName"]

    # Fallback: Name field
    if entry.get("Name"):
        return entry["Name"]

    # Last resort
    return str(entry.get("Id", ""))


def convert(data):
    output = {}

    for key, value in data.items():
        output[str(key)] = {
            "Id": value.get("Id"),
            "RecountName": get_recount_name(value),
            "DamageId": value.get("DamageId", []),
        }

    return output
