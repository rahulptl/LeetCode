import scala.collection.mutable

object Solution {
    def romanToInt(s: String): Int = {
        var mapping : mutable.HashMap[String, Int] = mutable.HashMap(
            "I" -> 1,
            "V" -> 5,
            "X"-> 10,
            "L"-> 50,
            "C"-> 100,
            "D"-> 500,
            "M"-> 1000
        )
        var int_value = 0
        var prev_value =0
        var current_value = 0
        for(character<-s.reverse){
            current_value = mapping(character.toString)
            if(current_value < prev_value){
                int_value-=current_value
            }
            else{
                int_value+=current_value
            }
            prev_value = current_value
        }
        int_value
    }
}