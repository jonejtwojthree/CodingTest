import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] array) {
return (int)Arrays.stream(Arrays.stream(array).mapToObj(el->el+"").collect(Collectors.joining()).split("")).filter(el->el.equals("7")).count();
       
    }
}