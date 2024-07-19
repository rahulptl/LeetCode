object Solution {
    def longestCommonPrefix(strs: Array[String]): String = {

        def is_prefix(length:Int): Boolean = {

        var prefix = strs(0).substring(0,length)
        strs.forall(_.startsWith(prefix))

        }

        var start = 0
        var end = strs.map(_.length).min
        var mid = (start+end)/2

        while(start<=end){
        if(is_prefix(mid)){
            start = mid+1
        }else{
            end = mid-1
        }
        mid = (start+end)/2
        }

        strs(0).substring(0,mid)

  }
}