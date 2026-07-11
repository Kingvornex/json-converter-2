def convert(data):
    return {
        key: data[key]
        for key in sorted(data.keys(), key=lambda x: int(x))
    }
