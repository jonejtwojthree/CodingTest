function solution(my_string) {
  return my_string
    .split("")
    .map((el) =>
      el === el.toLowerCase() ? el.toUpperCase() : el.toLowerCase()
    )
    .join("");
}
