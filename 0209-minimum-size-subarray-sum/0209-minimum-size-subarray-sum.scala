object Solution {
      def minSubArrayLen(target: Int, nums: Array[Int]): Int = {

      var current_sum = 0
      var start = 0
      var min_size = Int.MaxValue

      for(end<-nums.indices){

        current_sum = current_sum+nums(end)

        while(current_sum>=target){
          min_size = Math.min(min_size, (end-start+1))
          current_sum = current_sum - nums(start)
          start+=1
        }

      }

      if(min_size==Int.MaxValue){
        return 0
      }
    else{
        return min_size
      }

  }
}