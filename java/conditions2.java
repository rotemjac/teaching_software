import java.util.Scanner;
public class conditions2 {

	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		//the first way
		
		int number1;
		
		System.out.println("enter a number between 0 and 10");
		number1=in.nextInt();
   	
		if(number1 <0) {System.out.println("this number is too small");} 
	    else if(number1>10){System.out.println("this number is too big");}
	    else if( number1<10||number1<0) {System.out.println("good number");}
		
		
  //the second way
		
		int number2;
		
		System.out.println("enter a number between 10 and 20");
		number2=in.nextInt();
		
		switch(number2){
		
		case number2<10:
			System.out.println("this number is too small");
		
		}

		
	}

}
