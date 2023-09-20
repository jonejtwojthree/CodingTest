function solution(order) {
  return order
    .toLocaleString()
    .split("")
    .filter((el) => parseInt(el) % 3 == 0 && parseInt(el)).length;
}

// return [...order.toString().matchAll(/[3|6|9]/g)].length;
