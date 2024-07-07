import scala.collection.mutable

object Solution {
    def majorityElement(nums: Array[Int]): Int = {
    var candidate = -1
    var counter = 0

    for (i<-nums){
    if (counter==0){
      candidate=i
    }

    if(i==candidate){
        counter+=1
    }
    else{
        counter-=1
    }

    }

    counter=0
    for (i<-nums){
      if (i==candidate){
        counter+=1
      }
    }

    if(counter>nums.length/2){
      candidate
    }else{
      -1
    

  }
    }
}