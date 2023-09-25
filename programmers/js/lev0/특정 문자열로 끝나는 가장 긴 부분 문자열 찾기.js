function solution(myString, pat) {
  let idx = myString.length - pat.length;
  while (idx >= 0) {
    if (myString.substring(idx, idx + pat.length) === pat) break;
    idx -= 1;
  }
  return myString.substring(0, idx + pat.length);

  //     return str.substring(0, str.lastIndexOf(pat)) + pat;\
}
