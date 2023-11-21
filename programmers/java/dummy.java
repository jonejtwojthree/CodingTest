package programmers.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class dummy {
    public static void main(String[] args){
        Map<Character, Integer> dict = new HashMap<>();
        for(int i=97;i<=122;i++)
            dict.put((char)i, i-96);
        
        int[] result = new int[26];

        String my_string = "Programmers".toLowerCase();
        for(var c : my_string.toCharArray())
        {
            result[dict.get(c)]+=1;
        }
        
        System.out.println(Arrays.toString(result));
    }


}
