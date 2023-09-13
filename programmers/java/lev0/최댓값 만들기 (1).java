import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        return numbers[numbers.length-1] * numbers[numbers.length-2];
    }
}


// Int[]를 Integer[]로 만드는 법 -> Arrays.stream(int[]).boxed().toArray(Integer[]::new)
// 내림차순으로 sort정책 변경 -> compare인터페이스 오버라이딩

// class Solution {
//     public int solution(int[] numbers) {
//         Integer[] arr =Arrays.stream(numbers).boxed().toArray(Integer[]::new);
        
//         Arrays.sort(arr, new Comparator<Integer>() {
//             public int compare(Integer a, Integer b){
//                 return b-a;
//             }
//         });
        
//         return arr[0] * arr[1];
//     }
// }