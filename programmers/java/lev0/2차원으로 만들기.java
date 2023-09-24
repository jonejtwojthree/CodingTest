import java.util.stream.IntStream;
class Solution {
    public int[][] solution(int[] num_list, int n) {
        return IntStream.range(0, num_list.length / n)
                .mapToObj(i -> IntStream.range(0, n)
                        .map(j -> num_list[i * n + j])
                        .toArray())
                .toArray(int[][]::new);
    }
}

// class Solution {
//     public int[][] solution(int[] num_list, int n) {
//         int[][] answer = {};

//         int length = num_list.length;

//         answer = new int[length/n][n];

//         for(int i=0; i<length; i++){
//             answer[i/n][i%n]=num_list[i];
//         }

//         return answer;
//     }
// }