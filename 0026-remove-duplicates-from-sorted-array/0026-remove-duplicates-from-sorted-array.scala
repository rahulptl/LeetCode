object Solution {
    def removeDuplicates(nums: Array[Int]): Int = {
        //var nums = Array(0,0,1,1,1,2,2,3,3,4)
        var sp = 0

        for ( fp <- nums.indices){
            println(s"sp $sp fp $fp")
            if (fp<nums.length-1 && nums(sp) != nums(fp+1)){
            sp+=1
            nums(sp) = nums(fp+1)
            }
        }

        sp+1
    }
}