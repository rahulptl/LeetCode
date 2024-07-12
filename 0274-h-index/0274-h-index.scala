object Solution {
    def hIndex(citations: Array[Int]): Int = {

    var countCitations = Array.fill(citations.length+1)(0)

    for(i<-citations){
      if (i>citations.length){
        countCitations(citations.length) +=1
      }
      else{
        countCitations(i)+=1
      }
    }

    var idx = 0
    var total = 0
    for(i<-countCitations.length-1 to 0 by -1 if idx==0){
      total+=countCitations(i)
      if(total>=i){
        print(idx)
        idx = i
      }
    }
    idx


  }
}