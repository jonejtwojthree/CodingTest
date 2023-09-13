function solution(my_string) {
  return my_string
    .split("")
    .reduce((acc, el) => acc + (!isNaN(parseInt(el)) ? parseInt(el) : 0), 0);
  return [...my_string].reduce(
    (acc, el) => acc + (!isNaN(parseInt(el)) ? parseInt(el) : 0),
    0
  );
}
