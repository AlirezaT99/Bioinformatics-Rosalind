import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String pattern = scanner.nextLine(),
                text = scanner.nextLine();
        int maxMismatch = scanner.nextInt();
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < text.length() - pattern.length() + 1; i++)
            if (hammingDistance(pattern, text.substring(i, i + pattern.length())) <= maxMismatch)
                result.append(i).append(" ");
        System.out.println(result.toString().trim());
    }

    private static int hammingDistance(String pattern, String text) {
        int result = 0;
        for (int i = 0; i < pattern.length(); i++)
            result += pattern.charAt(i) != text.charAt(i) ? 1 : 0;
        return result;
    }
}