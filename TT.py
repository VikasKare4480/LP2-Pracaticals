import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        System.out.println("Enter a Text: ");
        Scanner input = new Scanner(System.in);
        String plaintext = input.next();
        System.out.println("Enter a Key: ");
        String key = input.next();
        int colLength = key.length();
        int rowLength = (plaintext.length() + key.length()) / key.length();
        char[][] matrix1 = new char[rowLength][colLength];
        int init = 0;
        for (int i = 0; i < rowLength; i++) {
            for (int j = 0; j < colLength; j++) {
                if (init < plaintext.length())
                    matrix1[i][j] = plaintext.charAt(init);
                init++;
            }
        }

        for (int j = 0; j < colLength; j++) {
            for (int i = 0; i < rowLength; i++) {
                int p = key.charAt(j) - '1';
                System.out.print(matrix1[i][p]);
            }
        }

        
       
    }
}