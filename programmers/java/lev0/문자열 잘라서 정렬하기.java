import java.util.Arrays;
import java.util.stream.Stream;
class Solution {
    public String[] solution(String myString) {
        String[] answer = {};
        return Arrays.stream(myString.split("x")).filter(s -> !s.isEmpty()).sorted().toArray(String[]::new);
    }
}