function f(s) {
  answer = "";
  for (let i = 0; i < s.length; i++) {
    if (i % 2 == 0) {
      answer += s[i].toUpperCase();
    } else {
      answer += s[i].toLowerCase();
    }
  }
  return answer;
}
function solution(s) {
  let arr = s.split(" ");

  let answer = arr.map((el) => f(el)).join(" ");
  console.log(answer);
  return answer;
}
