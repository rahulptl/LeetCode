import scala.collection.mutable
object Solution {
    def isAnagram(s: String, t: String): Boolean = {


        var shm = mutable.HashMap[Char, Int]().withDefaultValue(0)



        for(c<-s){
        shm.update(c, shm.getOrElse(c,0)+1)
        }
        for(i<-t){
        shm.get(i) match {
            case Some(b) => shm.update(i, b-1)
            case _ => shm.update(i,-1)
        }
        }
        var output=true

        shm.values.forall(_==0)

  }
}