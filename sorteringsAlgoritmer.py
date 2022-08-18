import random, copy

# def bogoSort(items):
#     # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
#     items = items.copy()
#     isSorted = None # Boolean til markering af, om listen er sorteret
#     attempts = 0 # Tællevariabel til at holde styr på antal af forsøg
#     while not isSorted:
#         attempts += 1
#         if attempts > len(items) * 5000: # Check for at stoppe tendensen mod uendeligt
#             print('Giver op på grund af for mange forsøg ({}) og bruger TimSort'.format(attempts))
#             items.sort()
#             return items
#         random.shuffle(items) # Bland alle elementer helt tilfældigt
#         isSorted = True # Vi går ud fra at listen tilfældigvis er sorteret,
#         # ...og prøver i denne løkke at bevise det modsatte
#         for index in range(len(items)-1):
#             if items[index] > items[index+1]:
#                 isSorted = False
#                 break # Bryd løkken hvis et eneste element er forkert sorteret
#     print('Sorteret efter {} forsøg'.format(attempts))
#     return items


def insertionSort(items):
    # Vi laver et for loop for hver værdi i listen
    for i in range(len(items)):
        # For at ikke løbe in i fejl tjekker vi at det ikke er den første element i listen
        if not i == 0:
            # så laver vi et nyt for loop som kører ned af arrayet fra det punkt (i) vi er for at se om der skal byttes værdi
            for c in range(i):
                # For at ikke løbe in i fejl tjekker vi at det ikke er den første element i listen
                if not i - c == 0:
                    # så tjekker vi om den forrige værdi er større end nuværende
                    #i-c fordi så går vi mod starten af arrayet så vi tjekker om ændret værdi er lavere en andre
                    if items[(i - c) - 1] > items[(i - c)]:
                        # vis sandt gemmer vi forrige værdi i switch
                        switch = items[(i - c) - 1]
                        # Og sætter forrige element til nuværende værdi
                        items[(i - c) - 1] = items[(i - c)]
                        # Og sætter nuværende element til switch(forige værdi)
                        items[(i - c)] = switch
                    else:
                        #vis der ikke skal byttes noget stopper vi loopet og går videre i listen mod slutningen
                        break
    return items

if __name__ == '__main__':
    l = list(range(0, 10))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = insertionSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)
