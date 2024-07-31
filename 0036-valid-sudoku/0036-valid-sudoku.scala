import scala.collection.mutable.ArrayBuffer
object Solution {
    def isValidSudoku(board: Array[Array[Char]]): Boolean = {

        var rows  = ArrayBuffer.fill(9)(ArrayBuffer.empty[Char])
        var columns = ArrayBuffer.fill(9)(ArrayBuffer.empty[Char])
        var box = ArrayBuffer.fill(9)(ArrayBuffer.empty[Char])
        var isValid = true
        for(i<-0 until 9 if isValid){
        for(j<-0 until 9 if isValid){

            if(board(i)(j)!='.'){

            val box_number = (( i / 3 ) *3 )+(j/3)
            var temp = board(i)(j)
            if(rows(i).contains(temp)){
                isValid=false

            }
            if(columns(j).contains(temp)){
                isValid=false
            }
            if(box(box_number).contains(temp)){
                isValid=false
            }
            
            rows(i)+=temp 
            columns(j)+=temp
            box(box_number)+=temp
            }

        }
        }
        
        return isValid


  }
}