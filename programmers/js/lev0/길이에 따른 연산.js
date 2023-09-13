function solution(num_list) {
  return num_list.length >= 11
    ? num_list.reduce((agg, el) => agg * el, 1)
    : num_list.reduce((agg, el) => agg + el, 0);
}
