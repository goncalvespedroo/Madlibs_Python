print("___________(adjective): Once upon a time, in a ___________(adjective) land far, far away, there lived a ______(noun). This ______(noun) was known far and wide for their ___________(adjective) ______(noun). People came from _______(place) just to witness the ______(noun)'s ___________(adjective) ______(noun).____(name), a ___________(adjective) _________(occupation), heard about this ______(noun) and decided to ______(verb) to see it for themselves. They packed their ______(noun) and set off on a ___________(adjective) journey.Along the way, ____(name) encountered a ___________(adjective) ______(noun) who offered them a ______(noun) in exchange for ______(verrb + ing). ____(name) accepted the offer and continued on their ___________(adjective) way.Finally, after ________(number) days of ______(verrb + ing), ____(name) arrived at the ______(noun) of the ______(noun). They were greeted by a ___________(adjective) ______(noun) who invited them to join in a game of ______(noun).____(name) couldn't resist the opportunity to play, and they had a ___________(adjective) time. They laughed so hard that _________(pronoun) _______(verb + ed) for hours.As the sun set on this ___________(adjective) day, ____(name) realized that sometimes the most ___________(adjective) adventures happen when you least expect them. With a ______(noun) full of memories, ____(name) _______(verb + ed) back home, knowing that they would never forget their ___________(adjective) journey to the land of the ______(noun).")

proceed = input("Proceed? y/n ")
if proceed == "n":
    print("Okay, bye bye!")
else:
    adjective = input("Add an adjective: ")
    noun = input("Add a noun: ")
    place = input("Add a place: ")
    name = input("Add a name: ")
    occupation = input("Add an occupation: ")
    verb = input("Add a verb: ")
    number = input("Add a number: ")
    ing_verb = input("Add an ing verb: ")
    pronoun = input("Add a pronoun: ")
    ed_verb = input("Add a ed verb: ")

    

    print(f"{adjective} : Once upon a time, in a {adjective} land far, far away, there lived a {noun} . This {noun} was known far and wide for their {adjective} {noun} . People came from {place} just to witness the {noun} 's {adjective} {noun} . {name} , a {adjective} {occupation} , heard about this {noun} and decided to {verb} to see it for themselves. They packed their {noun} and set off on a {adjective} journey.Along the way, {name} encountered a {adjective} {noun} who offered them a {noun} in exchange for {ing_verb} . {name} accepted the offer and continued on their {adjective} way.Finally, after {number} days of {ing_verb} , {name} arrived at the {noun} of the {noun} . They were greeted by a {adjective} {noun} who invited them to join in a game of {noun} .{name} couldn't resist the opportunity to play, and they had a {adjective} time. They laughed so hard that {pronoun} {ed_verb} for hours.As the sun set on this {adjective} day, {name} realized that sometimes the most {adjective} adventures happen when you least expect them. With a {noun} full of memories, {name} {ed_verb} back home, knowing that they would never forget their {adjective} journey to the land of the {noun} .")