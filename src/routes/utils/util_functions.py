def format_modifiers(modifiers_str, modifiers):
    if modifiers_str:
        for m in modifiers_str.split(","):
            if m:
                modifiers.append(int(m))
    return modifiers