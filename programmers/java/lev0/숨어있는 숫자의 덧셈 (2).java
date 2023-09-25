import java.util.Arrays;

class Solution {
    public int solution(String my_string) {
//         var s = my_string.split("[a-zA-Z]");
//         int answer = 0;
//         for(var str :s ){
//             if(!str.equals("")){
//                 answer += Integer.valueOf(str);
//             }
//         }
//         return answer;
    
        return Arrays.stream(my_string.split("[A-Z|a-z]")).filter(s -> !s.isEmpty()).mapToInt(Integer::parseInt).sum();

    }
    
}