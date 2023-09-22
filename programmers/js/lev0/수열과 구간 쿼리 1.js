function solution(arr, queries) {
  queries.forEach((row) => {
    for (let i = row[0]; i <= row[1]; i++) {
      arr[i] += 1;
    }
  });
  return arr;

  //  queries.forEach(([s, e]) => {
  //     while (s <= e) arr[s++]++;
  // });
  // return arr
}
