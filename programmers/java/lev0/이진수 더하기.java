class Solution {
    public String solution(String bin1, String bin2) {
        return Integer.toBinaryString(Integer.parseInt(bin1,2) + Integer.parseInt(bin2,2));

   }
    
    static int b2int(String s){
        String[] tmp = s.split("");
        int length = tmp.length;

        int num=0;
        for(int i=0;i<length;i++){
            num += (int)Math.pow(2.0, (length-i-1))*Integer.parseInt(tmp[i]);
        }
        return num;

    }


    static String int2b(int num){
        String tmp="";
        while(num>0){
            tmp+=Integer.toString(num%2);
            num/=2;
        }
        
        return new StringBuffer(tmp).reverse().toString();
    }
}