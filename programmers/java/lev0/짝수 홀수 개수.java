import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
       int[] arr = {0,0};
        for(int num: num_list){
            arr[num%2]+=1;
        }        
        return arr;
        // int[] temp = {Arrays.stream(num_list).filter(num->num%2==0).toArray().length, Arrays.stream(num_list).filter(num->num%2==1).toArray().length};
        // return temp;
        
    }
}