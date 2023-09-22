import java.util.stream.IntStream;
import java.util.Arrays;
class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        Arrays.stream(queries).forEach(row->IntStream.range(row[0], row[1]+1).forEach(i->arr[i]+=1));
        return arr;
    }
}