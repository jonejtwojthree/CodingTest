class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        for(String el : my_string.split(""))
            answer +=(el.repeat(n));
        
        return answer;
    }
}

// class Solution {
//     public String solution(String my_string, int n) {
//         StringBuilder sb = new StringBuilder();
//         for(char c : my_string.toCharArray()){
//             sb.append((c + "").repeat(n));
//         }
//         return sb.toString();
//     }
// }
