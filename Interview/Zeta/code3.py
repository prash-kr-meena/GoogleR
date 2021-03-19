from Utils.Array import input_array

"""

Q2. 
You are given a n-ary tree with every node representing a currency and every edge is weighted 
with weight given as the conversion rate of parent node currency to its child node currency,
 
 then you are given with n queries with each query consisted of the given currency and its amount, 
 you have to translate this currency to the new currency and tell how much amount you will get
 
           dollar
   *70 /       |*0.8   \*0.9
  rs.        pound     euro
   |*.04                  | *2
  Dinar                   xyz

M queries
rs 10 -> dollar   = 0.7 dollar
euro 50 -> rs                  ---> dollar to rs  (ie find conversion rate)      and  then going from dollar to euro (finding its conversion rate) 
pound 20 -> euro                          0.9                                                     70
                                          / 0.9                                              ---> * 70
                                          
dinar 40  -> xyz     

                        dollar to dinar conversion                            to xyz
                            70 * 0.04   --> total multiplier                   




               dollar
      *70 /       |*0.8   \*0.9
     rs.        pound     euro
   |       |      
   |*2      |  * 0.04
  xyz       dinar  
   

dinar 40  -> xyz              dollar to dinar                      then               dollar to xyz
                             70 * 0.04   --> total multiplier                          70 * 2
              

Time
O(n) for tree traversal
O(M) to answer all the M queries
total = O(m + n)


Space 
O(n) space for mapi  : so that we can answer our M queriey in o(1) time



M Times
current_currency   amount       conversion_Currency
"""

if __name__ == '__main__':
    input_array()
    pass
