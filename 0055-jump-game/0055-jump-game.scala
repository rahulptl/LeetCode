object Solution {
  def canJump(nums: Array[Int]): Boolean = {
    var target = nums.length-1
    for (i <-nums.length-1 to 0 by -1 ){
      if (nums(i)+i >= target){
        target = i
      }
    }

    if(target==0){
      true
    }
    else{
      false
    }
  }
}