import json
def remove_duplicates():
    result = []
    seen = set()

    with open("result.json", encoding="utf-8") as file:
        items = json.load(file)

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    cleanData = sorted(set(result))
    return cleanData
