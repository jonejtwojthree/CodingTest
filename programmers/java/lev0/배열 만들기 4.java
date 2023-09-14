import java.util.ArrayList;
class Solution {
    public int[] solution(int[] arr) {      
        ArrayList<Integer> arrayList = new ArrayList<>();
		int i=0;

		while(i<arr.length){
			if(arrayList.size()==0){
				arrayList.add(arr[i++]);
			}else{
				if(arrayList.get(arrayList.size()-1) < arr[i]){
					arrayList.add(arr[i++]);
				}else{
					arrayList.remove(arrayList.size()-1);
				}
			}

		}
        
        int idx = 0;
        int[] stk = new int[arrayList.size()];
        for (int data : arrayList)
            stk[idx++] = data;
        return stk;
            }
}