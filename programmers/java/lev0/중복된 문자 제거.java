import java.util.Arrays;
import java.util.stream.*;
class Solution {
    public String solution(String my_string) {
        return String.join("",Arrays.stream(my_string.split("")).distinct().toArray(String[]::new));
        // return my_string.chars().mapToObj(Character::toString).distinct().collect(Collectors.joining());
        
        
        
        //String[] answer = my_string.split("");
        // Set<String> set = new LinkedHashSet<String>(Arrays.asList(answer));
        // return String.join("", set);
    }
}