class Person:
    def __init__(self, name, preference):
        self.name = name
        self.pref_list = preference
        self.partner = None
        self.pref_index = 0

    def __str__(self):
        return self.name

def stable_marriage(n, men_prefs, women_prefs):
    men = {}
    women = {}
    for i in range(n):
        men[str(i+1)] = Person(str(i+1), men_prefs[i])
        women[str(i+1)] = Person(str(i+1), women_prefs[i])

    free_men = men.copy()

    while free_men:
        man_name = list(free_men.keys())[0]
        man = free_men[man_name]
        woman_name = man.pref_list[man.pref_index]
        woman = women[woman_name]
        if woman.partner is None:
            man.partner = woman
            woman.partner = man
            del free_men[man_name]
        else:
            current_partner = woman.partner
            if woman.pref_list.index(current_partner.name) > woman.pref_list.index(man_name):
                current_partner.partner = None
                free_men[current_partner.name] = current_partner
                woman.partner = man
                man.partner = woman
                del free_men[man_name]
            else:
                man.pref_index += 1
    for woman in women.values():
        print(woman.partner.name, woman.name)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        men_prefs = []
        women_prefs = []
        for _ in range(n):
            men_prefs.append(input().split()[1:])
        for _ in range(n):
            women_prefs.append(input().split()[1:])
        stable_marriage(n, men_prefs, women_prefs)
