package AOC.day9;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import AOC.Day;

public class Day9 extends Day{

	ArrayList<String> cities;
	int[][] distances;
	
	@Override
	public void readInput() {
		List<String> lines = readInputAsStrings(9);
		/*List<String> lines = Arrays.asList("London to Dublin = 464", 
				"London to Belfast = 518",
				"Dublin to Belfast = 141");
		*/
		HashSet<String> citySet = new HashSet<>();
		
		for (String s : lines) {
			String[] parts = s.split(" ");
			citySet.add(parts[0]);
			citySet.add(parts[2]);
		}  
		
		cities = new ArrayList<String>(citySet);
		distances = new int[cities.size()][cities.size()];
		
		System.out.println(cities);
		
		for (String s : lines) {
			String[] parts = s.split(" ");
			distances[cities.indexOf(parts[0])][cities.indexOf(parts[2])] = Integer.parseInt(parts[4]);
			distances[cities.indexOf(parts[2])][cities.indexOf(parts[0])] = Integer.parseInt(parts[4]);
		} 
		
		for (int i=0; i<distances.length; i++) {
			System.out.println(Arrays.toString(distances[i]));
		}
				
	}

	@Override
	public void part1() {
		List<List<String>> combinations = new ArrayList<List<String>>();
		collectCombinations(cities, new ArrayList<String>(), combinations);
		
		int minDistance = Integer.MAX_VALUE;
		
		for(int i=0; i<combinations.size(); i++) {
			int distance = 0;
			for(int j=0; j<combinations.get(i).size()-1; j++) {
				int x = cities.indexOf(combinations.get(i).get(j));
				int y = cities.indexOf(combinations.get(i).get(j+1));
				distance += distances[x][y];
				if(distance > minDistance) {
					break;
				}
			}
			minDistance = Math.min(distance,minDistance);
		}
		
		System.out.println("Min distance " + minDistance);
	}

	private void collectCombinations(List<String> cities, List<String> selection, List<List<String>> result) {
		if(selection.size() == cities.size()) {
			result.add(selection);
			return;
		}
		
		for(int i=0; i<cities.size(); i++) {
			List<String> sel = new ArrayList<String>(selection);
			if (!sel.contains(cities.get(i))) {
				sel.add(cities.get(i));
				collectCombinations(cities, sel, result);
			}
		}
	}
	
	@Override
	public void part2() {
		List<List<String>> combinations = new ArrayList<List<String>>();
		collectCombinations(cities, new ArrayList<String>(), combinations);
		
		int maxDistance = Integer.MIN_VALUE;
		
		for(int i=0; i<combinations.size(); i++) {
			int distance = 0;
			for(int j=0; j<combinations.get(i).size()-1; j++) {
				int x = cities.indexOf(combinations.get(i).get(j));
				int y = cities.indexOf(combinations.get(i).get(j+1));
				distance += distances[x][y];
			}
			maxDistance = Math.max(distance,maxDistance);
		}
		
		System.out.println("Max distance " + maxDistance);		
	}

	
}
