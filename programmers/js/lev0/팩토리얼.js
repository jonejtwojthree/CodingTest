function solution(n) {
  let i = 1;
  let num = 1;

  while (num <= n) {
    i += 1;
    num *= i;
  }
  return i - 1;
}
