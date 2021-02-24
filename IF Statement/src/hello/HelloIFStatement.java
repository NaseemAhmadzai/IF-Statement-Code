package hello;
import java.util.Scanner; 
public class HelloIFStatement {
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Secret(); 
        
	}

	private static void Secret() {
		final String MAGIC_PASSWORD = "dragon";
		Scanner sc = new Scanner(System.in); 
		System.out.print("What is the Password:"); 
		String guess = sc.next();
		if (guess == MAGIC_PASSWORD){
			 System.out.println("You guessed it!");{
		  } 
	   {
		   
		   System.out.println("You failed.");
	    } 
	}
	}
	}
	


