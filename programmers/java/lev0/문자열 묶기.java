import java.util.*;
class Solution {
    public int solution(String[] strArr) {
        
        ArrayList<String> a = new ArrayList<>();
        Map<Integer, ArrayList<String>> map = new HashMap<>();
        for(var value: strArr){
            if(map.get(value.length()) == null){
                map.put(value.length(), new ArrayList<>());
            }
            map.get(value.length()).add(value);

        }
        
       int answer = 0;
        for (int len : map.keySet())
            answer = Math.max(answer, map.get(len).size());

        return answer;
    }
}