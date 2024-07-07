import scala.collection.mutable

object Solution {
    def majorityElement(nums: Array[Int]): Int = {

    var hashMap = new mutable.HashMap[Int, Int]()
    var found = false
    var me = -1
    for (i<-nums if !found){
      val counter = hashMap.getOrElse(i,0) + 1
      if (counter>nums.length/2){
        found=true
        me = i
      }
      hashMap.put(i, counter)
      println(hashMap)
    }

    me
  }
}