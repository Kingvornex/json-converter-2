def convert(data):
    result = {}

    for key, entry in data.items():
        names = entry.get("Names", {})

        name = (
            names.get("en")
            or entry.get("Name")
            or names.get("zh-CN")
            or str(entry.get("Id", key))
        )

        result[str(entry.get("Id", key))] = name

    return result
