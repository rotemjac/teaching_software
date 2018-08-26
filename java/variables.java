import java.util.Scanner;
public class variables {

	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		
		double a=4;
		int b=5;
		int c=7;
		int d=15;
		String str="hellow evryone";
		
		System.out.println(b/a);
		
		System.out.println(d/c);
		//Not working because one of the variables have to be casting
		System.out.println((double)d/c);
		System.out.println(str);
		
		
		
		
		
	}
}