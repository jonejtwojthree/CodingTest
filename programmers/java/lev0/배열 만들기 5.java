import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) { 
        List<Integer> answer = new ArrayList<>();
        
        for (String str : intStrs) {
            // Integer n = Integer.valueOf(str.substring(s, s+l));
            int n = Integer.parseInt(str.substring(s, s+l));
            if(n> k){
                answer.add(n);
            }
        }
        // return answer.stream().mapToInt(Integer::intValue).toArray();
        return answer.stream().mapToInt(i->i).toArray();
    }
}
