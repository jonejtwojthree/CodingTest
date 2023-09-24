function solution(num_list, n) {
  //     let answer = [];

  //     for (let i = 0; i <num_list.length; i = i + n) {
  //         answer.push(num_list.slice(i, i + n));
  //         console.log(num_list.slice(i, i + n));
  //     }

  // return answer
  return Array(num_list.length / n)
    .fill([])
    .map(() => num_list.splice(0, n));
}
