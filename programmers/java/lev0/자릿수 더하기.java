class Solution {
    public int solution(int n) {
        int answer = 0;
        for(String el : Integer.toString(n).split(""))
            answer += Integer.parseInt(el);
        return answer;
    }
}