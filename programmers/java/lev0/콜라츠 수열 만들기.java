import java.util.ArrayList;
class Solution {
    public int[] solution(int n) {
        var answer = new ArrayList<Integer>();
        answer.add(n);
        int i=0;
        while((int)answer.get(i)!=1){
            boolean b = answer.get(i) % 2 == 0 ? answer.add(answer.get(i) / 2) : answer.add(answer.get(i) * 3 + 1);
            i+=1;

        }
        return answer.stream().mapToInt(el->el).toArray();

        
    }
}