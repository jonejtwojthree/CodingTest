class Solution {
    public int solution(String my_string) {
        int answer = 0;
        for(String s : my_string.split("")){
            try{
                answer += Integer.parseInt(s);
            }catch(java.lang.NumberFormatException e){} 
        }
        return answer;
    }
}

// stream을 이용해서 구하기
// 
class Solution {
    public int solution(String myString) {
        return myString.chars().mapToObj(i -> (char) i).filter(Character::isDigit).map(String::valueOf).mapToInt(Integer::valueOf).sum();
    }
}
