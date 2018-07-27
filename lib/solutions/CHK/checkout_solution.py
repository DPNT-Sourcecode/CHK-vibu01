from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
   allowed_sku_list = ['A','B','C','D','E']
   list_of_skus = list(skus)

   for sku in list_of_skus:
       if sku not in allowed_sku_list:
           return -1

   count_of_skus = dict(Counter(list_of_skus))
   price = {"A":50,"B":30,"C":20,"D":15,"E":40}
   cost = 0

   def multi_offer(sku,quanity, price,cost):
       number_of_sku = count_of_skus[sku]
       sku_offer_count = (number_of_sku / quanity)
       cost += (sku_offer_count) * price
       if sku_offer_count >= 1:
           remainder = count_of_skus[sku] % quanity
           count_of_skus[sku] = remainder
       return cost

   cost = multi_offer("A",3,130,cost)
   cost = multi_offer("B", 2, 45, cost)






   print count_of_skus
   for sku,value in count_of_skus.iteritems():
        cost += value *price[sku]


   return cost

print checkout("AAAEE")




