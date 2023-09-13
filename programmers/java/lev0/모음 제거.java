import java.util.stream.Collectors;
import java.util.stream.Stream;
class Solution {
    public String solution(String my_string) {
        // return my_string.chars().filter(el->el !='a'&& el !='i'&& el !='u'&& el !='e'&& el !='o').mapToObj(Character::toString).collect(Collectors.joining());
        return my_string.replaceAll("[aeiouAEIOU]", "");

    }
}