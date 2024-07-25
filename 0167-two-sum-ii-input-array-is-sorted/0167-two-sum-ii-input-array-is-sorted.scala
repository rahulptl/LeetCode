object Solution {
      def twoSum(numbers: Array[Int], target: Int): Array[Int] = {

      var lp = 0
      var rp = numbers.length-1
      var found = false
      var left_result = -1
      var right_result = -1
      while(lp<rp & !found){

        val sum = numbers(lp) + numbers(rp)

        if(sum==target){
          found=true
          left_result = lp
          right_result = rp
        }
        if(sum<target){
          lp+=1
        }
        if(sum>target) {
          rp -= 1
        }

      }

      Array(left_result+1, right_result+1)

  }
}