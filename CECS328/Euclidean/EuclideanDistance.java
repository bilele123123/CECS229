package Euclidean;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class EuclideanDistance {
    public static void main(String[] args) {
        List<double[]> points = new ArrayList<>();

        // Read points from a file
        try (BufferedReader br = new BufferedReader(new FileReader("H:\\Document\\CSULB Spring 23\\CECS229\\CECS229\\CECS328\\1.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                // Extract coordinates from the line and add them to the list
                String[] parts = line.trim().replaceAll("[{}]", "").split(",");
                double x = Double.parseDouble(parts[0].trim());
                double y = Double.parseDouble(parts[1].trim());
                System.out.println("Parsed: x=" + x + ", y=" + y);
                points.add(new double[]{x, y});
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Function to calculate the Euclidean distance between two points
        double minDistance = calculateMinimumDistance(points);

        // Print the minimum distance
        System.out.println("Minimum Euclidean Distance: " + minDistance);
    }

    public static double euclideanDistance(double[] point1, double[] point2) {
        double x1 = point1[0];
        double y1 = point1[1];
        double x2 = point2[0];
        double y2 = point2[1];
        return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
    }

    public static double calculateMinimumDistance(List<double[]> points) {
        double minDistance = Double.MAX_VALUE;
        double threshold = 1e-9; // Adjust the threshold as needed
    
        for (int i = 0; i < points.size(); i++) {
            for (int j = i + 1; j < points.size(); j++) {
                double[] point1 = points.get(i);
                double[] point2 = points.get(j);
                double distance = euclideanDistance(point1, point2);
                
                if (distance < threshold) {
                    // Points are very close, consider them equal
                    return 0.0;
                }
                
                minDistance = Math.min(minDistance, distance);
            }
        }
    
        return minDistance;
    }
    
}
