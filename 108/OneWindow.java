// Most programming languages of today have most of the "hadean" (my word) programming constructs abstracted away into things called "packages", which you "import" into a program. In the case of the Java programming language, the "swing" package calls upon the window manager on the operating system in question.
// 
// The code below creates a basic window with button in it. Despite the code below being the same, if you run the program on different operating systems (more specifically, on machines with a different window manager), you result in a different-looking window. 
import javax.swing.*;
import java.awt.event.*;

public class SampleJavaWindow {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Sample Java Window");
        frame.setSize(260, 150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // frame.setLayout(null);

        JLabel label = new JLabel("Hello there!");

        JButton okButton = new JButton("General Kenobi!");
        okButton.setBounds(50, 35, 160, 50);

        frame.add(okButton);

        frame.setVisible(true);
    }
}