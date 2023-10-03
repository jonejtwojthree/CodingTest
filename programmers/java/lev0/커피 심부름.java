import java.util.*;
class Solution {
    public int solution(String[] order) {
        Map<String, Integer> menu = new HashMap<>();

        menu.put("americano", 4500);
        menu.put("iceamericano", menu.get("americano"));
        menu.put("americanoice", menu.get("americano"));
        menu.put("hotamericano", menu.get("americano"));
        menu.put("americanohot", menu.get("americano"));

        menu.put("cafelatte", 5000);
        menu.put("icecafelatte", menu.get("cafelatte"));
        menu.put("cafelatteice", menu.get("cafelatte"));
        menu.put("hotcafelatte", menu.get("cafelatte"));
        menu.put("cafelattehot", menu.get("cafelatte"));

        menu.put("anything", menu.get("iceamericano"));
                
        int answer = 0;
        for(var s:  order){
            if(menu.containsKey(s)){
                answer += menu.get(s);
            }
        }
        return answer;
    }
}

class Solution {
    public int solution(String[] order) {
        int answer = 0;
        for (String eachOrder : order) {
            if (eachOrder.contains("americano") || eachOrder.equals("anything"))
                answer += 4500;
            else 
                answer += 5000;
        }
        return answer;
    }
}