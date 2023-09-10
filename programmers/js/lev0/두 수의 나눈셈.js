function solution(num1, num2) {
  // floor 내림 , trunc 버림
  var answer = Math.floor((num1 / num2) * 1000);
  // var answer = Math.trunc((num1 / num2) * 1000);

  return answer;
}

console.log(solution(1, 16));
