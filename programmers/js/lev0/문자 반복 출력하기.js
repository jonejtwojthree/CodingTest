function solution(my_string, n) {
  return my_string
    .split("")
    .map((el) => el.repeat(n))
    .join("");
}

// 구조분해할당!!!!!!!!!!!!!!!!
function solution(my_string, n) {
  return [...my_string].map((el) => el.repeat(n)).join("");
}
