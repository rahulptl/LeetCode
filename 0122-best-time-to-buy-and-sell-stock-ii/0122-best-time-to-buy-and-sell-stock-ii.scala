object Solution {
  def maxProfit(prices: Array[Int]): Int = {

    var profit = 0
    var sp = 0
    for (fp<-1 until prices.length){
      if(prices(fp) >= prices(sp)){
        profit = profit + (prices(fp) - prices(sp))
      }
      sp+=1
    }

    profit

  }
}