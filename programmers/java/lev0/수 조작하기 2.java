import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
class Solution {
    public String solution(int[] numLog) {
        Map<Integer, String> dict = new HashMap<>();
        
        dict.put(1,"w");
        dict.put(-1,"s");
        dict.put(10,"d");
        dict.put(-10,"a");
        
        String answer="";
        for(int i=1;i<numLog.length;i++){
            answer+=dict.get(numLog[i]-numLog[i-1]);
        }
        return answer;
    }
}