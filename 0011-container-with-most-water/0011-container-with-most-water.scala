object Solution {
    def maxArea(height: Array[Int]): Int = {

        var max_volume = 0

        var lp = 0
        var rp = height.length - 1

        while(lp<rp){

        val current_volume = math.min(height(lp), height(rp)) * (rp-lp)
        max_volume = math.max(current_volume, max_volume)
        if(height(lp)<=height(rp)){
            lp+=1
        }
        else{
            rp-=1
        }

        }
        max_volume
  }
}