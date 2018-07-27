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


   if "A" in list_of_skus:
    number_of_a = count_of_skus["A"]
    number_of_a = 0
    a_offer_count = (number_of_a / 3)
    cost = (a_offer_count) * 130
    if a_offer_count >= 1:
        remainder = count_of_skus["A"] % 3
        print "remainder" + str(remainder)
        count_of_skus["A"] = remainder

   try:
       number_of_b= count_of_skus["B"]
   except KeyError:
       number_of_b = 0






   b_offer_count =  (number_of_b / 2)
   cost =  cost + (b_offer_count) * 45

   if b_offer_count >= 1:
       try:
            remainder = count_of_skus["B"] % 2

            count_of_skus["B"] = remainder
       except KeyError:

           pass

   print count_of_skus
   for sku,value in count_of_skus.iteritems():
        print value
        cost += value *price[sku]


   return cost

checkout("BBBB")




