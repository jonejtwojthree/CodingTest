function solution(arr, flag) {
  let answer = [];

  flag.forEach((el, i) => {
    if (el) {
      for (let j = 0; j < arr[i] * 2; j++) answer.push(arr[i]);
    } else {
      for (let j = 0; j < arr[i]; j++) answer.pop();
    }
  });
  return answer;

  //   return arr.reduce(
  //     (prev, num, i) => (flag[i] ? [...prev, ...new Array(num * 2).fill(num)] : prev.slice(0, -num)),
  //     [],
  //   );
}
