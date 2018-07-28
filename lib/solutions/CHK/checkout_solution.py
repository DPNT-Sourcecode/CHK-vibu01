from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
   allowed_sku_list = ['A','B','C','D','E',"F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W",
                       "X","Y","Z"]
   list_of_skus = list(skus)

   for sku in list_of_skus:
       if sku not in allowed_sku_list:
           return -1

   count_of_skus = dict(Counter(list_of_skus))
   print count_of_skus
   price = {"A":50,"B":30,"C":20,"D":15,"E":40,"F":10,"G":10,"H":10,"I":35,"J":60,"K":80,"L":90,"M":15,"N":40,"O":10,
            "P":50,"Q":30,"R":50,"S":30,"T":20,"U":40,"V":50,"W":20,"X":90,"Y":10,"Z":50}
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


   def multi_offer_one_free_same(sku,quanity):
       number_of_sku = count_of_skus[sku]
       sku_offer_count = (number_of_sku / quanity)
       if sku_offer_count >= 1:
           remainder = count_of_skus[sku] % quanity
           print "remainder " + str(remainder)
           if remainder == 0:
               count_of_skus[sku] = count_of_skus[sku] - (sku_offer_count-1)
           else:
               count_of_skus[sku] = count_of_skus[sku] - sku_offer_count
       return cost


   if "A" in list_of_skus:
        while count_of_skus["A"] >= 3:
            if count_of_skus["A"] >= 5:
                cost = multi_offer("A", 5, 200, cost)

            if count_of_skus["A"] >= 3:
                cost = multi_offer("A",3,130,cost)

   print cost

   if "H" in list_of_skus:
        while count_of_skus["H"] >= 5:
            if count_of_skus["H"] >= 10:
                cost = multi_offer("H", 10, 80, cost)

            if count_of_skus["H"] >= 5:
                cost = multi_offer("H",5,45,cost)

   print cost

   if "P" in list_of_skus:
        while count_of_skus["P"] >= 5:

            if count_of_skus["P"] >= 5:
                cost = multi_offer("P",5,200,cost)

   print cost

   if "Q" in list_of_skus:
        while count_of_skus["Q"] >= 3:

            if count_of_skus["Q"] >= 3:
                cost = multi_offer("Q",3,80,cost)

   print cost

   if "V" in list_of_skus:
        while count_of_skus["V"] >= 2:
            if count_of_skus["V"] >= 3:
                cost = multi_offer("V", 3, 130, cost)

            if count_of_skus["V"] >= 2:
                cost = multi_offer("V",2,90,cost)

   print cost

   if list_of_skus.count("K") >= 2:
       while count_of_skus["K"] >= 2:
           cost = multi_offer("K", 2, 150, cost)

   if list_of_skus.count("N") >= 3 and list_of_skus.count("M"):
       print "N was found " + str(list_of_skus.count("N")) + " times."
       apply_count = list_of_skus.count("N") / 3
       print "The N offer can be applied " + str(apply_count)

       multi_offer_one_free("N", 3, "M")

   if list_of_skus.count("R") >= 3 and list_of_skus.count("Q"):
       print "R was found " + str(list_of_skus.count("R")) + " times."
       apply_count = list_of_skus.count("R") / 3
       print "The R offer can be applied " + str(apply_count)

       multi_offer_one_free("R", 3, "Q")




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
       multi_offer_one_free_same("F", 2)

   if list_of_skus.count("U") >= 4:
       print "U was found " + str(list_of_skus.count("U")) + " times."
       multi_offer_one_free_same("U", 3)




   print "The final cost is " + str(cost)
   print count_of_skus
   for sku,value in count_of_skus.iteritems():

        cost += value *price[sku]
        print sku + " " +str(value) + " x " + str(price[sku])


   return cost

