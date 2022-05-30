
def find_anagrams(ana_one, ana_two):

    if sorted(ana_one) == sorted(ana_two):
        return True
    else:
        return False


#test code
print(find_anagrams("listen", "silent"))

#@George Akor
#theStormGod

