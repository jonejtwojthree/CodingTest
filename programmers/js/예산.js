function solution(d, budget) {
  d.sort((a, b) => a - b);

  let answer = 0;
  let sum = 0;

  for (el of d) {
    if (sum + el <= budget) {
      answer += 1;
      sum += el;
    } else {
      break;
    }
  }
  return answer;
}

///////////////////////////////////////////////
function solution(d, budget) {
  return d
    .sort((a, b) => a - b)
    .reduce((count, price) => {
      return count + ((budget -= price) >= 0);
    }, 0);
}
