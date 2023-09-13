function solution(my_string) {
  // return my_string.split("").map(el => el!='a' && el!='i' && el!='u' && el!='e' && el!='o' ? el:"").join("")

  // 정규표현식 /[]/g
  return string.replace(/[aeiou]/g, "");
}
