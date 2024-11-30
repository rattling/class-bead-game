def find_winners(items, key):
    max_value = max(key(item) for item in items)
    return [item for item in items if key(item) == max_value]
