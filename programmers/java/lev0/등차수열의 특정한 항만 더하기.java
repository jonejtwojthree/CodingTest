import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
    public int solution(int a, int d, boolean[] included) {
        // int answer = 0;
        // for(int i=0;i<included.length;i++){
        //     answer += included[i] ? d*i+a : 0;
        // }
        // return answer;
        return IntStream.range(0, included.length).map(idx -> included[idx]?a+(idx*d):0).sum();

    }
}