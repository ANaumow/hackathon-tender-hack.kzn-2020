import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        String url = "src/main/java/t.txt";
        String urlOutput = "src/main/java/o.txt";
        File outputFile = new File(urlOutput);
        Path path = Paths.get(url);
        Scanner scan = new Scanner(path);
        BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile));

        while (scan.hasNext()) {
            String str = scan.nextLine().toLowerCase();
            if(str.contains("[") && str.contains("]") || str.contains("добро пожаловать") || str.contains("обратитесь в нашу поддержку") ||
                    str.contains("оцените качество") || str.contains("обращение направлено") || str.contains("обратились в нашу техническую") ||
            str.contains("оператор включился") || str.contains("благодарим вас за обращение") || str.contains("спасибо за оценку") || str.equals("")){
                continue;
            }
            writer.write(str);
            writer.newLine();
            System.out.println(str);
        }
    }
}
