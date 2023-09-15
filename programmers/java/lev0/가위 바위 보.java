import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Solution {
    public String solution(String rsp) {
        Map<String, String> dict = new HashMap<>();
        dict.put("2", "0");
        dict.put("0", "5");
        dict.put("5", "2");
        
        return Stream.of(rsp.split("")).map(el->  dict.get(el)).collect(Collectors.joining(""));
        //         return Arrays.stream(rsp.split("")).map(s -> s.equals("2") ? "0" : s.equals("0") ? "5" : "2").collect(Collectors.joining());

    }
}