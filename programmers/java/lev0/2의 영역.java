class Solution {
    public int[] solution(int[] arr) {
        int first=0;
        int last=arr.length-1;
    
        for(int i=0;i<arr.length;i++){
            first=i;
            if(arr[i]==2){
                break;
            }
        }

        for(int i=last;i>=0;i--){
            last=i;
            if(arr[i]==2){
                break;
            }
        }
    
        if(first>last){
            return (new int[]{-1});
        }else{
            int[] tmp = new int[last-first+1];
            for(int i=first;i<=last;i++){
                tmp[i-first]=arr[i];
            }
            return (tmp);
        }

        //  List<Integer> list = Arrays.stream(arr).boxed().collect(Collectors.toList());
        // return list.contains(2) ? list.subList(list.indexOf(2), list.lastIndexOf(2) + 1) : Arrays.asList(-1);
    }
}