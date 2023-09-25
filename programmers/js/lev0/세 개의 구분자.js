function solution(myStr) {
  let tmp = myStr.split(/[abc]/g).filter((el) => el !== "");
  return tmp.length == 0 ? ["EMPTY"] : tmp;
}
