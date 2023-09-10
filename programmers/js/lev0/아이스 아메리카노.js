function solution(money) {
  //   var cup = ~~(money / 5500);
  //   return [cup, money - cup * 5500];
  return [Math.floor(money / 5500), money % 5500];
}
