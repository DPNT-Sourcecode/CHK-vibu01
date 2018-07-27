from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
   list_of_skus = list(skus)
   list_of_skus = [sku.upper() for sku in list_of_skus]
   count_of_skus = dict(Counter(list_of_skus))

   non_alphabetical_skus =  [sku for sku in skus if not sku.isalpha()]
   if non_alphabetical_skus:
       return -1

   price = {"A":50,"B":30,"C":20,"D":15}
   try:
       number_of_a= count_of_skus["A"]
   except KeyError:
       number_of_a = 0

   try:
       number_of_b= count_of_skus["B"]
   except KeyError:
       number_of_b = 0

   a_offer_count =  (number_of_b / 3)
   cost =  (a_offer_count) * 130

   if a_offer_count >= 1:
       remainder = count_of_skus["B"] % 3
       count_of_skus["A"] = remainder

   b_offer_count =  (number_of_b / 2)
   cost =  (b_offer_count) * 45

   if b_offer_count >= 1:
       remainder = count_of_skus["B"] % 2
       count_of_skus["B"] = remainder


   for sku,value in count_of_skus.iteritems():
        cost += value *price[sku]

   return cost




