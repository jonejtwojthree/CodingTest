function solution(n) {
  let answer = [n];
  let i = 0;
  while (answer[i] != 1) {
    answer[i] % 2 == 0
      ? answer.push(answer[i] / 2)
      : answer.push(answer[i] * 3 + 1);
    i += 1;
  }

  return answer;
}

// function solution(n, arr = []) {
//     arr.push(n)
//     if (n === 1) return arr
//     if (n % 2 === 0) return solution(n / 2, arr)
//     return solution(3 * n + 1, arr)
// }
