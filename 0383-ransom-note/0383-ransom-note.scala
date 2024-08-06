import scala.collection.mutable


object Solution {

    def canConstruct(ransomNote: String, magazine: String): Boolean = {

        var rhm = mutable.HashMap[Char, Int]()
        var mhm = mutable.HashMap[Char, Int]()

        for(char<-ransomNote){
            rhm.put(char, rhm.getOrElse(char, 0)+1)
        }

        for(char<-magazine){
        mhm.put(char, mhm.getOrElse(char,0)+1)
        }

        var output=true
        for((k,v)<-rhm if output){
        if(mhm.getOrElse(k,0)<v){
            output=false
        }
        }
    
        output
  }
}