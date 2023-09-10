function solution(angle) {
  return angle < 90 ? 1 : angle == 90 ? 2 : angle < 180 ? 3 : 4;
  // return [0, 90, 91, 180].filter((el) => el <= angle).length;
}
