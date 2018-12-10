package AOC.day11;

import java.util.Arrays;

import AOC.Day;

public class Day11 extends Day {

	char[] password;
	
	@Override
	public void readInput() {
		password = "hepxcrrq".toCharArray();
	}

	@Override
	public void part1() {
		while(!isPasswordOK()) {
			password[password.length-1] += 1;
			normalize();
		}
		System.out.println(Arrays.toString(password));
	}

	private void normalize() {
		if(password[password.length-1] > 'z') 
		for(int i = password.length-1; i >= 0; i--) {
			if(password[i] > 'z') {
				password[i] = 'a';
				if(i > 0) {
					password[i-1] += 1;
				}
			}			
		}
	}
	private boolean isPasswordOK() {
		boolean ok = true;
		
		for(int i = 0; i< password.length; i++) {
			if(password[i] == 'i' || password[i] == 'o' || password[i] == 'l')
				return false;
		}
		
		ok = false;
		for(int i = 0; i< password.length-2; i++) {			
			if (password[i]+1 == password[i+1])
				if (password[i]+2 == password[i+2]) {
					ok = true;
					break;
				}			
		}
		
		if (!ok)
			return false;
		
		for(int i=0; i<password.length-1; i++) {
			if(password[i] == password[i+1]) {
				for(int j=i+2; j<password.length-1; j++) {
					if(password[j] == password[j+1]) {
						return true;
					}
				}
			}
		}
		
		return false;
	}

	@Override
	public void part2() {
		
		while(!isPasswordOK()) {
			password[password.length-1] += 1;
			normalize();
		}
		
		password[password.length-1] += 1;
		
		while(!isPasswordOK()) {
			password[password.length-1] += 1;
			normalize();
		}
		System.out.println(Arrays.toString(password));
	}

}
