import java.util.*;
class Solution {
    public int solution(String s) {
       Stack<Integer> stack = new Stack<>();

        for(var str: s.split(" ")){
           if(str.equals("Z")){
               stack.pop();
           }else{
               stack.push(Integer.parseInt(str));
           }
       }

       return stack.stream().reduce((acc,el)->acc+el).orElse(0);
        
    }
}

// class Solution {
//     public int solution(String s) {
//         String[] strs = s.split(" ");
//         int length=strs.length;

//         int answer=0;
//         for(int i=0;i<length;i++){
//             answer += strs[i].equals("Z")?-1*Integer.parseInt(strs[i-1]):Integer.parseInt(strs[i]);
//         }
//         return answer;
//     }
// }