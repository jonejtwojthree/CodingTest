class Solution {
    public String solution(String my_string, int[] indices) {
        String[] strs = my_string.split("");
        for(int idx : indices){
            strs[idx]="";
        }
        strs.join
        return String.join("",strs);
    }
}function solution(my_string, indices) {
    //     let strs = my_string.split("");
    //     indices.forEach((el) => (strs[el] = ""));
    
    //     return strs.join("");
        
        return [...my_string].filter((_,i)=>!indices.includes(i)).join('');
    }