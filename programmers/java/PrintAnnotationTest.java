package programmers.java;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;


@interface AnnoTest{
 int id = 100;
//  String major(int i, int j); // 매개변수 사용 불가
//  String minor() throws Exception; // 예외 선언 불가
//  ArrayList<T> list(); // 타입 매개변수 정의 불가
}



enum TestType { 
    FIRST, SECOND;
}
@interface DateTime{
    String yymmdd();
    String hhmmss();
}

@Retention(RetentionPolicy.RUNTIME)
@interface TestInfo {
    int count() default 1;

    String testedBy();

    String[] testTools() default "JUnit"; // 배열 요소 (기본값 지정)

    TestType testType() default TestType.FIRST; // 상수 요소

    DateTime testDate(); // 어노테이션 요소
}

@SuppressWarnings("1111")  // 유효하지 않은 애너테이션은 무시된다.
@TestInfo(testedBy = "yeji", testDate = @DateTime(yymmdd = "20210202", hhmmss = "101055")) // 어노테이션 값 지정
public class PrintAnnotationTest {
    public static void main(String[] args) {
        Class<PrintAnnotationTest> cls = PrintAnnotationTest.class;

		// 어노테이션에 지정한 값들을 출력한다.
        TestInfo anno = cls.getAnnotation(TestInfo.class);
        System.out.println("anno.testedBy() : " + anno.testedBy());
        System.out.println("anno.testDate().yymmdd() : " + anno.testDate().yymmdd());
        System.out.println("anno.testDate().hhmmss() : " + anno.testDate().hhmmss());

        for(String str: anno.testTools()){
            System.out.println("testTools : "+str);
        }
        System.out.println();
    }
}