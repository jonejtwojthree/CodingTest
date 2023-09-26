import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Set;
class Solution {
    public String solution(String s) {
        List<String> list = new ArrayList<>();
        for(var tmp : s.split("")){
            if(s.lastIndexOf(tmp)==s.indexOf(tmp)){
                list.add(tmp);
            }
        }

        Collections.sort(list);
        return  String.join("",list);
    }
}