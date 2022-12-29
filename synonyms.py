import random

def synonyms():
    # Define a list of synonyms for the adjective
    synonyms = [
        "frisky", "energetic", "lively",
        "self-sufficient", "self-reliant", "self-sufficient",
        "clever", "bright", "quick-witted",
        "inquisitive", "inquiring", "wondering",
        "adorable", "charming", "attractive",
        "naughty", "playful", "roguish",
        "attractive", "pretty", "gorgeous",
        "velvety", "smooth", "silky",
        "soft", "downy", "feathery",
        "hairy", "wooly", "hairy",
        "dignified", "noble", "majestic",
        "smooth", "shiny", "polished"
    ]
    
    # Shuffle the list of synonyms
    random.shuffle(synonyms)

    text = "\n".join(synonyms)

    with open("synonyms.txt", "w") as f:
        f.writelines(text)
    # Return the first 30 synonyms
    return synonyms[0]

print(synonyms())