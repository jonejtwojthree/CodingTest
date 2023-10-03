function solution(order) {
  let answer = 0;
  order.forEach((el) => {
    if (el.includes("latte")) {
      answer += 5000;
    } else {
      answer += 4500;
    }
  });
  return answer;
}
