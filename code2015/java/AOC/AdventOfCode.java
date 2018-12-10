package AOC;

import java.util.Scanner;

public class AdventOfCode{
	
	public static void main(String[] args) {
		
		//We don't want to close System.in
		@SuppressWarnings("resource")
		Scanner s = new Scanner(System.in);
		
		try {
			System.out.println("Which day are we solving?");
			int day = s.nextInt();
			Day d = (Day)(Class.forName("AOC.day"+day+".Day"+day).newInstance());
			d.run();
		} catch ( Exception e ) {
			e.printStackTrace();
			System.out.println("That day has not been solved with Java");
		}
	}
}