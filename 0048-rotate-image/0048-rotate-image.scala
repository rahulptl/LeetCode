object Solution {
    def rotate(matrix: Array[Array[Int]]): Unit = {

    // transpose

        var n = matrix.length

        for(i<-0 until n){
            for(j<-0 until n){
                if(i>=j){
                val temp = matrix(i)(j)
                matrix(i)(j) = matrix(j)(i)
                matrix(j)(i) =  temp
            }
        }
        }

        for(i<-0 until n){

            var lp = 0
            var rp = n-1
            while(lp<=rp){
                val temp = matrix(i)(lp)
                matrix(i)(lp) = matrix(i)(rp)
                matrix(i)(rp) = temp
                    lp+=1
                    rp-=1
                }
        }



    }
}