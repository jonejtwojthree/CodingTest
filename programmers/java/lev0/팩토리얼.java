class Solution {
    public int solution(int n) {
        int i=1;
        int num=1;
        
        while(num<=n){
            i+=1;
            num*=i;
        }
        return i-1;
    }
}