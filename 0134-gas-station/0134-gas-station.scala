object Solution {
  def canCompleteCircuit(gas: Array[Int], cost: Array[Int]): Int = {

    var total_cost = 0
    var current_cost = 0
    var start_index = 0

    for(i<-gas.indices){

      total_cost = total_cost + gas(i) - cost(i)
      current_cost = current_cost + gas(i) - cost(i)

      if(current_cost<0){
        current_cost = 0
        start_index = i+1
      }

    }

    if(total_cost>=0){
      return start_index
    }
    return -1
  }
}