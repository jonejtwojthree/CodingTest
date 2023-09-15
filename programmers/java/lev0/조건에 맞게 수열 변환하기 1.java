import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        return Arrays.stream(arr).map(el->{return el>=50 && el%2==0 ? (int)el/2 : el < 50 && el%2==1 ? el*2 : el;}).toArray();
    }
}