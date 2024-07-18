farm_animals = {"sheep","hen","cow","horse","goat"}
wild_animals = {"lion","elephant","tiger","goat","panther","horse"}
#To do union of two sets we use union() method and | operator.Union is commutative
all_animals = farm_animals.union(wild_animals)
print(all_animals)
print(len(all_animals))
animals_all = farm_animals | wild_animals
print(animals_all)
print("-"*80)

from prescription_data import adverse_interactions

meds_to_watch = set()

for interaction in adverse_interactions:
    meds_to_watch = meds_to_watch.union(interaction)
    #we can also use .update() to rewrite a set
    meds_to_watch.update(interaction)
    #or |=
    meds_to_watch |= interaction

print(sorted(meds_to_watch))
