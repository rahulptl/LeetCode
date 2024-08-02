import scala.collection.mutable.ArrayBuffer

object Solution {
      
  def spiralOrder(matrix: Array[Array[Int]]): List[Int] = {

    var top = 0
    var bottom = matrix.length-1
    var left = 0
    var right = matrix(0).length-1
    var traversed : ArrayBuffer[Int]  = ArrayBuffer()

    while(top<=bottom & left<=right){
      
      for(j<-left to right){
        
        traversed+=matrix(top)(j)

      }
      top+=1
      
      for(j<-top to bottom){
        traversed+=matrix(j)(right)
      }
      right-=1
      
      if(top<=bottom){
        for(j<-right to left by -1){
          traversed+=matrix(bottom)(j)
        }
        bottom-=1
      }
      
      if(left<=right){
        for(j<-bottom to top by -1){
          traversed+=matrix(j)(left)
          
        }
        left+=1
      }

    }
    
    return traversed.toList

  }

}