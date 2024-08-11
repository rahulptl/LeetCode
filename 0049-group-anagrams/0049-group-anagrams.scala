import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer

object Solution {
  def groupAnagrams(strs: Array[String]): List[List[String]] = {
    // Initialize the HashMap without using withDefaultValue
    val output = mutable.HashMap[String, ArrayBuffer[String]]()

    // Iterate over each string in the array
    for (string <- strs) {
      // Sort the string to form the key
      val temp = string.sorted

      // If the key doesn't exist, create a new ArrayBuffer and add it to the map
      if (!output.contains(temp)) {
        output(temp) = ArrayBuffer()
      }

      // Append the current string to the ArrayBuffer associated with the sorted key
      output(temp).append(string)
    }

    // Convert the map values (ArrayBuffers) to a list of lists
    output.values.map(_.toList).toList
  }

  def main(args: Array[String]): Unit = {
    val strs = Array("eat", "tea", "tan", "ate", "nat", "bat")
    val result = groupAnagrams(strs)
    println(result)
  }
}
