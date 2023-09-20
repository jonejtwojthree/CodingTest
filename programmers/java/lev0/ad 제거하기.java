import java.util.Arrays;
class Solution {
    public String[] solution(String[] strArr) {
        return Arrays.stream(strArr).filter(el->!el.contains("ad")).toArray(String[]::new);
    }
}