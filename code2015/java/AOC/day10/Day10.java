package AOC.day10;

import AOC.Day;

public class Day10 extends Day {

	String input;
	
	@Override
	public void readInput() {
		input = "3113322113";
		//input = "111221";
	}

	@Override
	public void part1() {
		String currInput = input;
		for (int i=0; i < 40; i++) {
			currInput = doLookAndSay(currInput);
		}
		System.out.println("Part1: "+currInput.length());
	}

	private String doLookAndSay(String digits) {
		StringBuilder sb = new StringBuilder();
		for(int i=0; i< digits.length(); i++) {
			char c = digits.charAt(i);
			int j = i;
			for(; j<digits.length() && digits.charAt(j) == c; j++);
			sb.append(j-i);
			sb.append(c);
			i = j-1;
		}
		return sb.toString();
	}

	@Override
	public void part2() {
		String currInput = input;
		for (int i=0; i < 50; i++) {
			currInput = doLookAndSay(currInput);
		}
		System.out.println("Part2: "+currInput.length());
	}

}
