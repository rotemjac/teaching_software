package conditions;
import java.util.Scanner;

public class If_Else_Example {
 
	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);

	int year;
	int month;
	int week;
	int day;
    double second;
	int check;
	
	
	
	System.out.println("enter the many that you earn per month");
	month=in.nextInt();
	
	year=month*12;
	week=month/4;
	day=week/5;
	//https://stackoverflow.com/questions/4931892/why-does-the-division-of-two-integers-return-0-0-in-java
	second=(double)(day)/28800;	
		
	System.out.println("If you want to see how much money you earn per\n" + 
		   "year press 1\n "
		  + "month press 2\n"
		  + "week press 3\n" 
		  + "day press 4\n"
		  +	"second press 5\n");
		  
		  check =in.nextInt();
 			
if (check == 1) {System.out.println( year);}
else if (check == 2){System.out.println(month);}
else if (check == 3) {System.out.println(week);}			
else if (check== 4) {System.out.println(day);}	
else if (check== 5) 	{System.out.println(second);}

	}
	}