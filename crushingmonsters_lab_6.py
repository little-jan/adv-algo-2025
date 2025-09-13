def potions(current_hp, potion_strength):
    new_hp = current_hp - (current_hp * potion_strength / 100)
    return new_hp

def swords(current_hp, sword_strength):
    new_hp = current_hp - sword_strength
    return new_hp

hp, no_potions, no_swords, no_items = input().split()
hp, no_potions, no_swords, no_items = int(hp), int(no_potions), int(no_swords), int(no_items)

if no_potions > 0:
    potion_potencies = list(map(int, input().split()))

if no_swords > 0:
    sword_strengths = list(map(int, input().split()))

potion_potencies.sort(reverse=True)
sword_strengths.sort(reverse=True)

min_hp = float('inf')

for k in range(min(no_items, no_swords) + 1):
    potions_used = min(no_items - k, no_potions)

    current_hp = hp
    for s in sword_strengths[:k]:
        current_hp = swords(current_hp, s)
    for p in potion_potencies[:potions_used]:
        current_hp = potions(current_hp, p)
    min_hp = min(min_hp, current_hp)

    current_hp = hp
    for p in potion_potencies[:potions_used]:
        current_hp = potions(current_hp, p)
    for s in sword_strengths[:k]:
        current_hp = swords(current_hp, s)
    min_hp = min(min_hp, current_hp)


min_hp = round(min_hp, 4)
print(min_hp)