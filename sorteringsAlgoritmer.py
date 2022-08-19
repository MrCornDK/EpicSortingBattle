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
    #vi laver et for loop der med en range af længden af arrayet
    for i in range(len(items)):
        # vi sætter nuværende værdi til  current
        current = items[i]

        # så laver vi en værdi for forrige index som bruges til at køre ned af listen mod starten
        f_i = i - 1
        # Så laver vi et loop som gælder vis forrige index ikke er større eller nul for at ikke få fejl og at forrige værdi er er stører end nuværende værdi
        while f_i >= 0 and current < items[f_i]:
            # så sætter vi nuværende  til forrige
            items[f_i+1] = items[f_i]
            # og så nedsætter vi forrige index med 1 og så kørrer loopet igen vis at f_i >= 0 and current < items[f_i] er true
            f_i -= 1
        # så sætter vi f_i + 1 til current for at færdig gøre switchne (fordi loopet bliver ikke kørst da f_1 er mindre end nul)
        items[f_i + 1] = current
    return items

def SelectionSort(itemsv2):
    for i in range(len(l)-1):
        min_index = i

        for j in range(i+1, len(l)-1):
            if l[j] < l[min_index]:
                min_index = j

        l[i], l[min_index] = l[min_index], l[i]
    return itemsv2

def bubbleSort(items):
    i = 0
    while i < len(items)-1:
        j = 0
        while j < len(items)-i-1:
            if items[j] > items[j+1]:
                current = items[j]
                items[j] = items[j+1]
                items[j+1] = current
            j += 1
        i += 1
    return items

def SelectionSort(itemsv2):
    for i in range(len(l)-1):
        min_index = i

        for j in range(i+1, len(l)-1):
            if l[j] < l[min_index]:
                min_index = j

        l[i], l[min_index] = l[min_index], l[i]
    return itemsv2

if __name__ == '__main__':
    b = [2, 1, 3, 8, 4, 5, 7, 9, 6, 0]
    print(b)
    print(bubbleSort(b))
    l = list(range(0, 10))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = bubbleSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)
