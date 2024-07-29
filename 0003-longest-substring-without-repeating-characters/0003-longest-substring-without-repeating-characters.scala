import scala.collection.mutable

object Solution {
    def lengthOfLongestSubstring(s: String): Int = {


        var mapping : mutable.HashMap[Char, Int]= mutable.HashMap()
        var start = 0
        var len = 0
        if(s.isEmpty || s.length==1){
        return s.length
        }
        for((char, index)<-s.zipWithIndex){
        
        if(mapping.contains(char) && (mapping(char)>=start)){
            start = mapping(char)+1
            
        }
        mapping(char) = index
        len = math.max(len, (index-start)+1)
        
        }
        len

  }
}