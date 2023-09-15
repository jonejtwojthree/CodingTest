import java.util.stream.Collectors;

class Solution {
    public String solution(String my_string) {
        return my_string.chars().mapToObj(el->(char)el).map(el->Character.isUpperCase(el) ? Character.toLowerCase(el): Character.toUpperCase(el)).map(Object::toString).collect(Collectors.joining());
        
    }
}