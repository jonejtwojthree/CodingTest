function solution(sides) {
  return Math.min(...sides) * 2 - 1;
  // sides.sort((a, b) => a - b);

  // let answer =
  //   sides[0] +
  //   sides[1] -
  //   (sides[1] + 1) +
  //   (sides[1] - (sides[1] - sides[0] + 1)) +
  //   1; //2*min-1
}
