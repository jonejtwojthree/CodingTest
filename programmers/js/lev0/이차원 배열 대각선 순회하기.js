function solution(board, k) {
  return board
    .flatMap((row, i) => row.filter((value, j) => i + j <= k))
    .reduce((acc, cur) => acc + cur, 0);

  //     return board.reduce(
  //   (total, row, i) =>
  //     total + row.reduce((prev, num, j) => (i + j <= k ? prev + num : prev), 0),
  //   0
  // );
}
