"""
find the first duplicate in an array [1,2,3,4,2,1]  ==> 2
do it in scala
"""

"""
import scala.collection.mutable.Map

def find_duplicate(arr: Array[Int]) : Int = {
 
  var freq:Map[Int,Int] = Map[Int,Int]()
 
  for(e <- arr) {
    val count: Int = freq.getOrElse(e,0);
    freq(e) = count+1
  }
  // println(freq)
 
  for(e <- arr) {
    val count: Int = freq.getOrElse(e,0);
    if(count > 1){
      return e
    }
  }
  return -1
}


var array = Array(1,2,3,3,2,4,5,2,6)
var duplicate = find_duplicate(array)

println("\n")
println(array.mkString(" "))
println(duplicate)
"""
