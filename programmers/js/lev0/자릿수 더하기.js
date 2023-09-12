function solution(n) {
  var answer = 0;

  [...n.toString()].map((el) => (answer += Number(el)));

  return answer;
}

// reduce 사용
function solution(n) {
  return n
    .toString()
    .split("")
    .reduce((acc, cur) => acc + Number(cur), 0);
}
