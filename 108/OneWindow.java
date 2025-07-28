// Most programming languages of today have most of the "hadean" (my word) programming constructs abstracted away into things called "packages", which you "import" into a program. In the case of the Java programming language, the "swing" package calls upon the window manager on the operating system in question.
// 
// The code below creates a basic window with button in it. Despite the code below being the same, if you run the program on different operating systems (more specifically, on machines with a different window manager), you result in a different-looking window. 
import javax.swing.*;
import java.awt.*;

/**
 * The Calculator class provides simple arithmetic operations.
 * 
 * @author 365 Days of Computer
 * @version 0.1
 */

public class OneWindow {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Sample Java Window");
        frame.setSize(260, 130);
        frame.setLayout(new BoxLayout(frame.getContentPane(), BoxLayout.Y_AXIS));

        JLabel label = new JLabel("Hello there!");
        JButton okButton = new JButton("General Kenobi!");

        label.setAlignmentX(Component.CENTER_ALIGNMENT);
        okButton.setAlignmentX(Component.CENTER_ALIGNMENT);

        frame.add(Box.createVerticalStrut(20));
        frame.add(label);
        frame.add(Box.createVerticalStrut(10));
        frame.add(okButton);

        frame.setVisible(true);
    }
    /**
    * @param  number_1  an integer
    * @param  number_2 another integer
    * @return      the image at the specified URL
    * @see         Image
    **/
    public int add_two_integers(int number_1, int number_2) {
        return number_1 + number_2;
    }
}