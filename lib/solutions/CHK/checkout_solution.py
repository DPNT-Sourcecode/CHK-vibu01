from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
   list_of_skus = list(skus)
   count_of_skus = dict(Counter(list_of_skus))
   print count_of_skus
checkout("ABCDABCD")