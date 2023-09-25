public class A로 B 만들기 {
    
}
import java.util.Arrays;
class Solution {
    public int solution(String before, String after) {
        char[] a = before.toCharArray();
        char[] b = after.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);

        var s =new String(a);
        
        System.out.println(s);
        return new String(a).equals(new String(b)) ? 1 :0;
    }
}
