// JS의 sort는 기본적으로 string 정렬을 위해 만들어 져서 int 비교 시에는 compare를 만들어야됨
function solution(numbers) {
  numbers.sort((a, b) => b - a);
  return numbers[0] * numbers[1];
}
