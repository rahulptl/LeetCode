object Solution {
    def reverseWords(s: String): String = {
        s.split(' ').filter(_.nonEmpty).reverse.mkString(" ")

    }
}