function solution(numLog) {
  let answer = "";

  let tmp = 0;
  for (let i = 0; i < numLog.length - 1; i++) {
    tmp = numLog[i + 1] - numLog[i];
    if (tmp == 1) {
      answer += "w";
    } else if (tmp == -1) {
      answer += "s";
    } else if (tmp == 10) {
      answer += "d";
    } else {
      answer += "a";
    }
  }
  return answer;
}
