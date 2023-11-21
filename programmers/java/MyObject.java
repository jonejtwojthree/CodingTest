package programmers.java;

public class MyObject {
    @MyAnnotation
    public void testMethod1(){
        System.out.println("testMethod11111임");
    }

    @MyAnnotation(qwer="My new Annotation")
    public void testMethod2(){
        System.out.println("testMethod2222임");
    }
}
