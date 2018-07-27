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


   def multi_offer(sku,quanity, price,cost):
       number_of_sku = count_of_skus[sku]
       sku_offer_count = (number_of_sku / quanity)
       cost += (sku_offer_count) * price
       if sku_offer_count >= 1:
           remainder = count_of_skus[sku] % quanity
           count_of_skus[sku] = remainder
       print cost
       return cost


   def multi_offer_one_free(sku,quanity,free_sku):
       number_of_sku = count_of_skus[sku]
       sku_offer_count = (number_of_sku / quanity)
       if sku_offer_count >= 1:
           remainder = count_of_skus[sku] % quanity
           count_of_skus[free_sku] = count_of_skus[free_sku] - sku_offer_count
       return cost

if count_of_skus["A"]
   if "A" in list_of_skus:
       if count_of_skus["A"] % 5 <= count_of_skus["A"] % 3:
           cost = multi_offer("A", 3, 130, cost)
       else:
           cost = multi_offer("A", 5, 200, cost)
   if "B" in list_of_skus:
    cost = multi_offer("B", 2, 45, cost)
   if "B" in list_of_skus:
    cost = multi_offer("B", 2, 45, cost)
   print count_of_skus
   if "E" in list_of_skus and "B" in list_of_skus:
    multi_offer_one_free("E",2,"B")






   print count_of_skus
   for sku,value in count_of_skus.iteritems():
        print value
        cost += value *price[sku]


   return cost


checkout("AAAAAAAA")
 #
 # - {"method":"checkout","params":["AAAAAAAA"],"id":"CHK_R2_021"}, expected: 330, got: 350
 # - {"method":"checkout","params":["AAAAAAAAA"],"id":"CHK_R2_022"}, expected: 380, got: 400
 # - {"method":"checkout","params":["EEEEBB"],"id":"CHK_R2_027"}, expected: 160, got: 145
 #
