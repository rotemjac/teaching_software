import java.util.Scanner;
public class MathActions {

	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		int	n1,n2,sum;
		String result;
		
		System.out.println("enter number one");
		n1=in.nextInt();
		System.out.println("enter number two");
		n2=in.nextInt();
		in.close();
		
		//1 - no return, just print
		sumNumbersAndPrint(n1,n2);
		
		//2 - return and assign to variable
		sum    = sumNumbersAndReturnAsInt(1,2);
		
		//3- return and pass as a parameter (or argument) to another function)
		result = sumNumbersAndReturnAsString(
				    sumNumbersAndReturnAsInt(1,2),
					n2
				);
		
		//4 - return and use inside an "if" statement
		if(sumNumbersAndReturnAsInt(1,2) == 3) {
			System.out.println("true");
		}
	}
	
	
	// ------------------------------------------------------------------------------------ //
	
	 static void sumNumbersAndPrint(int number2,int number1) {
		System.out.println(number1 + number2);
		
		
	}
	
	 static int sumNumbersAndReturnAsInt(int number2,int number1) {
		return number1 + number2;
	}	
	
	public static String sumNumbersAndReturnAsString(int number2,int number1) {
		return "The sum is: " +(number1 + number2);
	}
}