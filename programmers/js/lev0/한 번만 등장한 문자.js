function solution(s) {
  let dict = {};
  s.split("").forEach((el) => {
    dict[el] ? (dict[el] += 1) : (dict[el] = 1);
  });

  return Object.keys(dict)
    .filter((el) => dict[el] == 1)
    .sort()
    .join("");
}

function solution(s) {
  let res = [];
  for (let c of s) if (s.indexOf(c) === s.lastIndexOf(c)) res.push(c);
  return res.sort().join("");
}
