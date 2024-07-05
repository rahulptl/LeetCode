import scala.collection.mutable.ArrayBuffer

object Solution {
    def removeElement(nums: Array[Int], `val`: Int): Int = {

        var sp = 0
        var a = `val`


        for (fp <- nums.indices ) {
            if (nums(fp)!=a){
                nums(sp) = nums(fp)
                sp+=1
            }
        }

        sp


    }
}