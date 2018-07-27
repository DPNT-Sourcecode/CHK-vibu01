from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
   list_of_skus = list(skus)
   count_of_skus = dict(Counter(list_of_skus))

   non_alphabetical_skus =  [sku for sku in skus if not sku.isalpha()]
   if non_alphabetical_skus:
       return -1

   
   number_of_A = count_of_skus["A"]
   number_of_B= count_of_skus["B"]
checkout("ABCDABCD")