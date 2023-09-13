import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int k) {
        return k%2 == 1 ? Arrays.stream(arr).map(el->el*k).toArray(): Arrays.stream(arr).map(el->el+k).toArray();
    }
}