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

   if "A" in list_of_skus:
    number_of_a = count_of_skus["A"]
    a_offer_count = (number_of_a / 3)
    cost += (a_offer_count) * 130
    if a_offer_count >= 1:
        remainder = count_of_skus["A"] % 3
        print "remainder" + str(remainder)
        count_of_skus["A"] = remainder
   print "cost " + str(cost)

   if "B" in list_of_skus:
    number_of_b = count_of_skus["B"]
    b_offer_count = (number_of_a / 2)
    cost +=  (b_offer_count) * 45
    if b_offer_count >= 1:
        remainder = count_of_skus["B"] % 2
        print "remainder" + str(remainder)
        count_of_skus["B"] = remainder








   print count_of_skus
   for sku,value in count_of_skus.iteritems():
        print value
        cost += value *price[sku]


   return cost

print checkout("AAABB")




