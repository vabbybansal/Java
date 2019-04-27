package sorts;

public class mergeSort{
	
	static public int[] myArray = {8,7,6,10,20,2000,5,4,3,2,1,9};
		
	public static String arrayToString(){
		int len = myArray.length;
		StringBuilder str = new StringBuilder();
		
		str.append("[");
		for(int i=0; i<len; i++){
			str.append(myArray[i] + ",");
		}
		str.append("]");
		
		return str.toString();

	}
	
	public static String arrayToString(int[] myArray){
		int len = myArray.length;
		StringBuilder str = new StringBuilder();
		
		str.append("[");
		for(int i=0; i<len; i++){
			str.append(myArray[i] + ",");
		}
		str.append("]");
		
		return str.toString();

	}
	
	
	public int[] myMergeSort(int[] myArray)
	{
	
		int len = myArray.length;
		if(len == 1)
		{
			//Recurrence base condition: Stop Recurrence
			return (myArray);
		}
		
		int leftLen, rightLen;
		leftLen = len/2;
		rightLen = (len % 2 == 0) ? leftLen : leftLen + 1;
				
		int[] leftArray = new int[leftLen];
		int[] rightArray = new int[rightLen];
		//break array into 2 parts
		System.arraycopy(myArray, 0, leftArray, 0, leftLen);
		System.arraycopy(myArray, leftLen, rightArray, 0, rightLen);
		
		
		//Recurrence
		leftArray = myMergeSort(leftArray);
		rightArray = myMergeSort(rightArray);
		
		
		//Merge while backtracking
		int[] finalArray = new int[len];
		finalArray = merge(leftArray, rightArray);
		
		return finalArray;//returns the merged array
	}
	
	public int[] merge(int[] a, int[] b){
		
		int lenA = a.length;
		int lenB = b.length;
		int lenFinal = lenA + lenB;
		int[] finalArray = new int[lenFinal];
		
		int counterA = 0;
		int counterB = 0;
		
		//Two Finger Algorithm
		for(int i=0;i<lenFinal;i++)
		{
			if(counterA == lenA)
			{
				finalArray[i] = b[counterB++];
			}
			else if(counterB == lenB)
			{
				finalArray[i] = a[counterA++];
			}
			else
			{
				if(a[counterA] <= b[counterB])
				{
					finalArray[i] = a[counterA++];
				}
				else
				{
					finalArray[i] = b[counterB++];
				}
			}
			
		}
		
		return finalArray;
	}
	
	
}