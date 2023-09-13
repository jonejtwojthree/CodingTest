import java.util.Arrays;
class Solution {
    public int solution(int[] array, int n) {
        return Arrays.stream(array).filter(el->el==n).toArray().length;
    }
}