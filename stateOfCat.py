def stateOfCat():
    # Define the list of verbs and adverbs
    lines = [
        "Running swiftly",
        "Pouncing playfully",
        "Leaping gracefully",
        "Scampering quickly",
        "Stalking silently",
        "Hunting intently",
        "Playing excitedly",
        "Napping peacefully",
        "Purring contentedly",
        "Grooming meticulously",
        "Sprinting energetically",
        "Chasing gleefully",
        "Prowling stealthily",
        "Frolicking joyfully",
        "Relaxing lazily",
        "Gazing thoughtfully",
        "Lazing contentedly",
        "Wandering aimlessly",
        "Yawning widely",
        "Stretching luxuriously",
        "Mewing softly",
        "Curling up cozily",
        "Sleeping soundly",
        "Hissing menacingly",
        "Arching their back",
        "Flicking their tail",
        "Twitching their whiskers",
        "Knocking things over",
        "Rubbing against your leg",
        "Meowing loudly"
    ]
    
    text = "\n".join(lines)

    # Open a file in write mode
    with open("stateOfCat.txt", "w") as f:
        # Write the list of verbs and adverbs to the file
        f.writelines(text)

stateOfCat()