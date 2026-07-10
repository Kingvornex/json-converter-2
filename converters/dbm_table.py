# converters/dbm_table.py

NAME = "DBM Table Converter"

def convert(data):
    output = {}

    for key, entry in data.items():
        content = (
            entry.get("Contents", {}).get("en")
            or entry.get("Content")
            or entry.get("Contents", {}).get("zh-CN")
            or ""
        )

        output[str(entry["Id"])] = {
            "Id": entry["Id"],
            "CountCDTime": entry["CountCDTime"],
            "Content": content
        }

    return output
