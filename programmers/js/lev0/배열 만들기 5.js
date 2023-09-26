function solution(intStrs, k, s, l) {
  // var answer = [];
  // intStrs.forEach((el) => {
  //     let num = parseInt(el.slice(s, s + l));
  //     if (num > k) {
  //         answer.push(num);
  //     }
  // });
  // return answer;
  return intStrs.map((m) => +m.slice(s, s + l)).filter((m) => m > k);
}
