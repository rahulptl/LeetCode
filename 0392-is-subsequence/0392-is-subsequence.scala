object Solution {
    def isSubsequence(s: String, t: String): Boolean = {
        
        var it = t.iterator

        s.forall(it.contains)   
    }
}