import java.util.Scanner;


public class variables {
 
	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);

	int year;
	int month;
	int week;
	int day;
	int second;
	int check;
	int kind;
	
	
	
	System.out.println("enter the many that you earn per month");
	month=in.nextInt();
	
	year=month*12;
	week=month/4;
	day=week/5;
	second=day/28800;	
		
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