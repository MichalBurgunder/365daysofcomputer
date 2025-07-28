// Here we give an example of generating a JavaDoc, done using the javadoc
// software. To generate the documentation you need JavaDocs installed ("brew
// install javadocs" I assume, if you are on a mac) and then compile the file
// ("javac JavaDocExample.java") and run the command "javadoc -d java-docs
// JavaDocExample.java"

/**
 * This is a Basic class to illustrate the JavaDoc functionality. It has two
 * addition methods for the sake of showing off some features of JavaDoc. 
 * 
 * @author 365 Days of Computer
 * @version 0.1
 */
public class JavaDocExample {

    /**
    * A constructor for the class.
    **/
    public void JavaDocExample() {
        return;
    }
    /**
    * Our main function does nothing, as we simply need to illustrate JavaDoc.
    *  
    * @param  args  some hypothetical arguments
    **/
    public static void main(String[] args) {
        return;
    }
    /**
     * Adds two integers together
     * 
    * @param  number_1  an integer
    * @param  number_2 another integer
    * @return the sum of the two numbers
    **/
    public int add_two_integers(int number_1, int number_2) {
        return number_1 + number_2;
    }

    /**
    * Adds two floating point numbers together. 
    * 
    * @param  number_1  a floating point number
    * @param  number_2  another floating point number
    * @return the sum of the two floating point numbers
    **/
    public int add_two_floats(float number_1, float number_2) {
        return number_1 + number_2;
    }
}