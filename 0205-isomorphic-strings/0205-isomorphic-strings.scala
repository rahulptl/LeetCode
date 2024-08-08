import scala.collection.mutable
object Solution {
    def isIsomorphic(s: String, t: String): Boolean = {

        var mapping = mutable.HashMap[Char, Char]()
        var revMapping = mutable.HashMap[Char, Char]()
        var output = true
        for(idx<-t.indices){
            val a = s(idx)
            val b = t(idx)

            if(mapping.contains(a)){
                mapping.get(a) match {
                    case Some(mappedChar) => if (mappedChar != b) {
                    output = false
                    }
                    case _ => {}
                }
            }
            else{
                if(revMapping.contains(b)){
                    output=false
                }
                mapping.put(a,b)
                revMapping.put(b,a)
            }
        }
        output
    }
}