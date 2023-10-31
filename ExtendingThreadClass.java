import java.util.*;
// this is and example of threading by extending Thread class
class thread1 extends Thread {
    @Override // Here we have overrided the Run function which is defined in Thread.java Module
    public void run() {
        int i = 0;
        while (i < 400) {
            System.out.println("This is thread One");
            i++;
        }
    }
}

class thread2 extends Thread {
    @Override
    public void run() {
        int i = 0;
        while (i < 400) {
            System.out.println("This is thread Two");
            i++;
        }
    }
}

public class ExtendingThreadClass {

    public static void main(String[] args) {

        thread1 T1 = new thread1();
        thread2 T2 = new thread2();
        T1.start();
        T2.start();

    }

}