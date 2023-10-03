public class 문자 개수 세기 {
    
}
import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        Map<Character, Integer> dict = new HashMap<>();
        for(int i=65;i<=90;i++)
            dict.put((char)i, i-65);
        
        for(int i=97;i<=122;i++)
            dict.put((char)i, i-97+26);
        
        int[] result = new int[52];

        for(var c : my_string.toCharArray())
            result[dict.get(c)]+=1;

        return result;
    }
}