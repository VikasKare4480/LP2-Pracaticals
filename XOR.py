public class Main {

	public static void main(String[] args){
	    String str = "Hello World"; 
	    char arr[] = new char[11]; 
	    char arr1[] = new char[11]; 
	    System.out.println("Output of AND Operation"); 
	    for (int i = 0; i < str.length(); i++){
	        int value = str.charAt(i) & 127; 
	        char c = (char)value; 
	        System.out.println(c); 
	        arr[i] = c; 
	    }
		
		
        System.out.println("Output of AND Operation"); 
	    for (int i = 0; i < str.length(); i++){
	        int val = str.charAt(i) ^ 127; 
	        char b = (char)val; 
	        System.out.println(b); 
	        arr[i] = b; 
	    }
	}
}
