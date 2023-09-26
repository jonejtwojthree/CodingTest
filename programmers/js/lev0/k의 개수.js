function solution(i, j, k) {
  let answer = 0;
  while (i <= j) {
    answer += String(i)
      .split("")
      .filter((el) => el === String(k)).length;
    i += 1;
  }
  return answer;
}

function solution(i, j, k) {
  let a = "";
  for (i; i <= j; i++) {
    a += i;
  }
  return a.split(k).length - 1;
}
