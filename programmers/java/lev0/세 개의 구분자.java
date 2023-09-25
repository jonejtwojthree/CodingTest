import java.util.Arrays;
class Solution {
    public String[] solution(String myStr) {
         String[] tmp =  Arrays.stream(myStr.split("[abc]")).filter(el->!el.isEmpty()).toArray(String[]::new);
        return tmp.length == 0 ? new String[] { "EMPTY" } : tmp;
    }
}