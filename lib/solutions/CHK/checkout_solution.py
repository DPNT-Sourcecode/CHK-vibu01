from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
   allowed_sku_list = ['A','B','C','D','E',"F"]
   list_of_skus = list(skus)

   for sku in list_of_skus:
       if sku not in allowed_sku_list:
           return -1

   count_of_skus = dict(Counter(list_of_skus))
   print count_of_skus
   price = {"A":50,"B":30,"C":20,"D":15,"E":40,"F":10}
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

       return cost


   def multi_offer_one_free(sku,quanity,free_sku):
       number_of_sku = count_of_skus[sku]
       sku_offer_count = (number_of_sku / quanity)
       if sku_offer_count >= 1:
           remainder = count_of_skus[sku] % quanity
           count_of_skus[free_sku] = count_of_skus[free_sku] - sku_offer_count
       return cost

   if "A" in list_of_skus:
        while count_of_skus["A"] >= 3:
            if count_of_skus["A"] >= 5:
                cost = multi_offer("A", 5, 200, cost)

            if count_of_skus["A"] >= 3:
                cost = multi_offer("A",3,130,cost)

   print cost


   if list_of_skus.count("E") >= 2 and list_of_skus.count("B"):
       print "E was found " + str(list_of_skus.count("E")) + " times."
       apply_count = list_of_skus.count("E") / 2
       print "The E offer can be applied " + str(apply_count)

       multi_offer_one_free("E", 2, "B")

   try:
       if count_of_skus["B"] > 0:
           print "B was found " + str(list_of_skus.count("B")) + " times."
           apply_count = list_of_skus.count("B") / 2
           print "The B offer can be applied " + str(apply_count)

           for apply in range(0,apply_count):
               cost = multi_offer("B",2,45,cost)
               print count_of_skus
               print cost
   except KeyError:
       pass

   if list_of_skus.count("F") >= 3:
       print "F was found " + str(list_of_skus.count("F")) + " times."
       multi_offer_one_free("F", 2, "F")




   print "The final cost is " + str(cost)
   print count_of_skus
   for sku,value in count_of_skus.iteritems():

        cost += value *price[sku]
        print sku + " " +str(value) + " x " + str(price[sku])


   return cost

# - {"method":"checkout","params":["FFFF"],"id":"CHK_R3_042"}, expected: 30, got: 20
# - {"method":"checkout","params":["FFFFFF"],"id":"CHK_R3_043"}, expected: 40, got: 30
# - {"method":"checkout","params":["FFFFFF"],"id":"CHK_R3_044"}, expected: 40, got: 30#
print checkout("FFFF")