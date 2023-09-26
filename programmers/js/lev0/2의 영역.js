function solution(arr) {
  let a = arr.slice(arr.indexOf(2), arr.lastIndexOf(2) + 1);
  return a.length ? a : [-1];
}
