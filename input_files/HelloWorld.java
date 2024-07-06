// Java implementation of above approach
import java.util.*;

class GFG 
{

// Function to match character 
static boolean check(String s1, String s2) 
{
	// Create a map to map 
	// characters of 1st string 
	Map<Character, Integer> mp = new HashMap<>();

	// traverse the first string 
	// and create a hash map 
	for (int i = 0; i < s1.length(); i++)
	{
		mp.put(s1.charAt(i), mp.get(s1.charAt(i)) == null ? 1 : mp.get(s1.charAt(i)) + 1);
	}

	// traverse the second string 
	// and if there is any 
	// common character than return 1 
	for (int i = 0; i < s2.length(); i++) 
	{
		if (mp.get(s2.charAt(i)) > 0) 
		{
			return true;
		}
	}

	// else return 0 
	return false;
}

// Driver code 
public static void main(String[] args)
{
	// Declare two strings 
	String s1 = "geeksforgeeks", s2 = "geeks";

	// Find if there is a common subsequence 
	boolean yes_or_no = check(s1, s2);

	if (yes_or_no == true)
	{
		System.out.println("Yes");
	} 
	else
	{
		System.out.println("No");
	}
}
}

/* This code contributed by PrinciRaj1992 */
