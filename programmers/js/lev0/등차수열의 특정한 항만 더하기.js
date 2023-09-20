function solution(a, d, included) {
  let answer = 0;
  included.forEach((el, i) => (el ? (answer += d * i + a) : 0));
  return answer;
}
