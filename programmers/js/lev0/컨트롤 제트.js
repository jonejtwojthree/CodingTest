function solution(s) {
  let stack = [];
  s.split(" ").forEach((el) => {
    if (el === "Z") stack.pop();
    else stack.push(parseInt(el));
  });
  return stack.reduce((acc, el) => acc + el, 0);
}
