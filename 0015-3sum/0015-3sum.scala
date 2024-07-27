object Solution {
  def threeSum(nums: Array[Int]): List[List[Int]] = {
    var result = Set[List[Int]]()
    val sortedNums = nums.sorted

    for (i <- sortedNums.indices if i < sortedNums.length - 2) {
      // Skip duplicate values for i
      if (i == 0 || sortedNums(i) != sortedNums(i - 1)) {
        val main_block = sortedNums(i)
        var sp = i + 1
        var fp = sortedNums.length - 1

        while (sp < fp) {
          val sum = main_block + sortedNums(sp) + sortedNums(fp)
          if (sum == 0) {
            result += List(main_block, sortedNums(sp), sortedNums(fp))
            while (sp < fp && sortedNums(sp) == sortedNums(sp + 1)) { sp += 1 }
            while (sp < fp && sortedNums(fp) == sortedNums(fp - 1)) { fp -= 1 }
            sp += 1
            fp -= 1
          }
          else if (sum < 0) {
            sp += 1
          }
          else {
            fp -= 1
          }
        }
      }
    }

    result.toList
  }
}