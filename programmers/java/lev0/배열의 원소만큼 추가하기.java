import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> solution(int[] arr) {
        return Arrays.stream(arr).boxed().flatMap(num -> Collections.nCopies(num, num).stream()).collect(Collectors.toList());
    }
}