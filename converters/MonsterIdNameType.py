def convert(data):
    result = {}

    for key, entry in data.items():
        names = entry.get("Names", {})

        if isinstance(names, dict):
            name = (
                names.get("en")
                or entry.get("Name")
                or names.get("zh-CN")
                or names.get("zh")
                or "Unknown"
            )
        else:
            name = entry.get("Name", "Unknown")

        result[str(entry.get("Id", key))] = {
            "MonsterType": entry.get("MonsterType", 0),
            "Name": name,
        }

    return result
