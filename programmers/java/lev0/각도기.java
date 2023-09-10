
import java.util.Arrays;

class Solution {
    public int solution(int angle) {
        int[] arr = {0,90,91,180};
        return Arrays.stream(arr).filter(el->el<=angle).toArray().length;
    }
}

