object Solution {
    def productExceptSelf(nums: Array[Int]): Array[Int] = {

    var prefix = Array.fill(nums.length)(0)
    var suffix = Array.fill(nums.length)(0)
    var output = Array.fill(nums.length)(0)
    prefix(0) = 1
    suffix(nums.length-1) = 1

    for(i<-1 until nums.length){
      prefix(i) = prefix(i-1)*nums(i-1)
    }
    for(i<-nums.length-2 until -1 by -1){
      suffix(i) = suffix(i+1) * nums(i+1)
    }

    for(i<-nums.indices){
      output(i) = prefix(i) * suffix(i)
    }

    output
        
    }
}