function solution(arr) {
  return arr.reduce((list, num) => [...list, ...new Array(num).fill(num)], []);

  //     let answer = []
  //     for(var el of arr){
  //         for(let i=0;i<el;i++)
  //             answer.push(el)

  //     }
  //     return answer
}
