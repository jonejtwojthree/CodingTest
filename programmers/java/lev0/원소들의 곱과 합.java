import java.util.Arrays;
import java.util.Optional;
import java.util.stream.Stream;

class Solution {
    public int solution(int[] num_list) {
        return Arrays.stream(num_list).reduce( (x,y) -> x*y).getAsInt() > (int)Math.pow( (double)(Arrays.stream(num_list).sum()), 2.0) ? 0:1;
    }
}