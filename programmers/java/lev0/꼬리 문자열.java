import java.util.Arrays;

class Solution {
    public String solution(String[] str_list, String ex) {
        var arr = Arrays.stream(str_list).filter(el->!el.contains(ex)).toArray(String[]::new);
		return String.join("", arr);
    //return Arrays.stream(strList).filter(s -> !s.contains(ex)).collect(Collectors.joining());

    }
}