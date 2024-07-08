object Solution {
  def reverse(nums:Array[Int], start:Int, end:Int):Unit = {
      var s = start
      var e =  end
      while(s<e){
        val temp = nums(s)
        nums(s) = nums(e)
        nums(e) = temp
        s +=1
        e -=1
      }

  }

  def rotate(nums:Array[Int], k:Int):Unit={
    var steps = k
    if(k>nums.length){
      steps = k%nums.length
    }

    reverse(nums, 0, nums.length-1)
    reverse(nums, 0, steps-1)
    reverse(nums, start=steps, nums.length-1)
    //println(nums.mkString(","))

  }
}