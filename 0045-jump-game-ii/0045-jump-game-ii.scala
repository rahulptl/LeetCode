object Solution {
      def jump(nums: Array[Int]): Int = {


    var current_end = 0
    var farthest = 0
    var jump = 0
    for ( i<-0 until nums.length-1){
      
      farthest = scala.math.max(farthest, nums(i)+i)
      
      if(i==current_end){
        jump+=1
        current_end = farthest
      }
    
      
    }
    
    jump
  }
}