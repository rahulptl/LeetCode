object Solution {
  def maxProfit(prices: Array[Int]): Int = {


    var sp = 0
    var profit = 0
    //println(prices.mkString(","))
    for(fp<-1 until prices.length){
      //println(s"$sp $fp $profit current_profit ${prices(fp)-prices(sp)}")
      if (prices(fp) - prices(sp) > 0) {
        profit = scala.math.max(profit, (prices(fp)-prices(sp)))
      }
      else{
        sp=fp
      }
    }

    profit

  }
}