import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer
import scala.util.Random
class RandomizedSet() {

    private val dict = mutable.HashMap[Int, Int]()
    private val list = ArrayBuffer[Int]()


    def insert(`val`: Int): Boolean = {
      if(dict.contains(`val`)){
        false
      }
      else{
        dict(`val`) = list.size
        list.append(`val`)
        true
      }
    }

    def remove(`val`: Int): Boolean = {

      if(!dict.contains(`val`)){
        false
      }
      else{
        val idx = dict(`val`)
        val lastElement = list.last
        list(idx) = lastElement
        dict(lastElement) =  idx
        list.dropRightInPlace(1)
        dict.remove(`val`)
        true
      }

    }

    def getRandom(): Int = {
      list(Random.nextInt(list.size))

    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * val obj = new RandomizedSet()
 * val param_1 = obj.insert(`val`)
 * val param_2 = obj.remove(`val`)
 * val param_3 = obj.getRandom()
 */