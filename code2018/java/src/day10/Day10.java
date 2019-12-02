package day10;

import java.applet.Applet;
import java.awt.BorderLayout;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Font;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.ScrollPane;
import java.awt.Scrollbar;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JFrame;


public class Day10 extends Applet{

	static List<Position> positions;
	public void init() {	
				
		positions = parseInput(readInput());
		
		System.out.println(positions);
		setLayout(new BorderLayout());
		ScrollPane s = new ScrollPane();
		s.setSize(100, 100);
		add("Center", s);
		
		MyCanvas canvas = new MyCanvas();
		s.add(canvas);
		
		
		canvas.setSize(5000, 3000);
	}
	
	public static List<String> readInput(){
		List<String> result = null;
		try {
			result = Files.readAllLines(new File(".")
					.getAbsoluteFile()
					.getParentFile().getParentFile().getParentFile()
					.toPath()
					.resolve("data").resolve("10.txt"));
			
		} catch (IOException e) {
			System.out.println("Failed to read input");
			e.printStackTrace();
		}
		return result;

	}
	
	public static List<Position> parseInput(List<String> input){
		//position=<-41766,  31541> velocity=< 4, -3>
		List<Position> result = new ArrayList<Position>();
		for (String s : input) {
			String[] position = s.substring(s.indexOf("<")+1,s.indexOf(">")).split(",");
			String[] velocity = s.substring(s.lastIndexOf("<")+1,s.lastIndexOf(">")).split(",");
			Position p = new Position(Integer.parseInt(position[0].trim()), Integer.parseInt(position[1].trim()), Integer.parseInt(velocity[0].trim()), Integer.parseInt(velocity[1].trim()));
			result.add(p);
		}
		return result;
	}
	static class Position{
		int x,y;
		int xVel, yVel;
		
		public Position(int x, int y, int xVelocity, int yVelocity) {
			this.x = x;
			this.y = y;
			this.xVel = xVelocity;
			this.yVel = yVelocity;
		}

		@Override
		public String toString() {
			return "[x=" + x + ", y=" + y + ", xVel=" + xVel + ", yVel=" + yVel + "]";
		}
		
		
	}
	static class MyCanvas extends Canvas {

		private static final long serialVersionUID = 1L;

		Image buffImage;
		Graphics offscreen;
		boolean initDone = false;

		MyCanvas() {
			super();
		}

		public void paint(Graphics g) {
			if (!initDone)
				initpaint(g);
			else
				g.drawImage(buffImage, 0, 0, this);
		}

		public void initpaint(Graphics g) {
			try {
				new BufferedImage(200000, 200000, BufferedImage.TYPE_BYTE_GRAY);
				buffImage = this.createImage(50000, 50000);
				offscreen = buffImage.getGraphics();
				offscreen.setColor(Color.black);
				offscreen.fillRect(0, 0, 6000, 6000);
				offscreen.setColor(Color.white);
				offscreen.setFont(new Font("Courier", Font.ITALIC, 42));
				offscreen.drawString("Hello World!", 0, 50);
				initDone = true;
				g.drawImage(buffImage, 0, 0, this);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	

}
