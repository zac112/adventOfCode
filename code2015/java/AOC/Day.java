package AOC;

import java.util.List;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

public abstract class Day{
	public final void run() {
		readInput();
		part1();
		part2();
	}
	
	public abstract void readInput();
	public abstract void part1();
	public abstract void part2();
	
	protected List<String> readInputAsStrings(int day){
		List<String> result = null;
		try {
			result = Files.readAllLines(new File(".")
					.getAbsoluteFile()
					.getParentFile().getParentFile()
					.toPath()
					.resolve("data").resolve(day+".txt"));
		} catch (IOException e) {
			System.out.println("Failed to read input");
		}
		return result;
	}
}