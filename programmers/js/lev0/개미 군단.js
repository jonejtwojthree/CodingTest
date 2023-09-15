function solution(hp) {
  // let arr = [5, 3, 1];
  // let answer = 0;
  // arr.forEach((el) => {
  //     answer += parseInt(hp / el);
  //     hp = hp % el;
  // });
  // return answer;

  // floor: 버림
  return Math.floor(hp / 5) + Math.floor((hp % 5) / 3) + ((hp % 5) % 3);
}
