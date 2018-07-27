from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
   list_of_skus = list(skus)
   count_of_skus = dict(Counter(list_of_skus))

   non_alphabetical_skus =  [sku for sku in skus if not sku.isalpha()]
   if non_alphabetical_skus:
       return -1

   price = {"A":50,"B":30,"C":20,"D":15}
   number_of_a = count_of_skus["A"]
   number_of_b= count_of_skus["B"]
   b_offer_count =  (number_of_b / 2)
   cost =  (b_offer_count) * 45
   print b_offer_count
   print cost

   if b_offer_count >= 1:
       remainder = count_of_skus["B"] % 2
       print remainder
       print count_of_skus["B"]
       if remainder != count_of_skus["B"]:
        count_of_skus["B"] = remainder
   print count_of_skus

   for sku in list_of_skus:
        cost += price[sku]
        print cost

checkout("ABB")


