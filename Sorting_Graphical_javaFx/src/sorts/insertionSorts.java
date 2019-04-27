package sorts;



public class insertionSorts{
	static public int[] myArray = {5,3,8,10,12,11,9,4,7,4,11,15,3,3,10,8,9,6,4};
//	static public int[] myArray = {1,11,10,2,0};
	public static final boolean USE_GRAPHIC = true; 
	public static final int ANIMATION_DELAY = 500;
	
	static int foundIndex = -1;
	
	public String toString(){
		int len = myArray.length;
		StringBuilder str = new StringBuilder();
		
		str.append("[");
		for(int i=0; i<len; i++){
			str.append(myArray[i]);
		}
		str.append("]");
		
		return str.toString();
	}
	
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
	
	public int[] insertionSortBasic(int[] myArray, int graphical){
		
		int length = myArray.length;
		int temp = 0;
		
		if(USE_GRAPHIC)
		{
			sortGraphic.insertionBasicUpdate(0, "blue");
		}
		for(int i=1; i<length; i++)
		{
			if(USE_GRAPHIC)
			{
				sortGraphic.insertionBasicUpdate(i, "blue");
				try {
					Thread.sleep(ANIMATION_DELAY);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			if(myArray[i] < myArray[i-1])
			{
				
				for(int j=i; j!=0; j--)
				{
					if(myArray[j] < myArray[j-1])
					{
						temp = myArray[j-1];
						myArray[j-1] = myArray[j];
						myArray[j] = temp;
						if(USE_GRAPHIC)
						{
							
							sortGraphic.insertionBasicUpdate(j-1, myArray[j-1]);
							sortGraphic.insertionBasicUpdate(j, myArray[j]);
							try {
								Thread.sleep(ANIMATION_DELAY);
							} catch (InterruptedException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
							
						}
						
					}
					else
					{
						
						break;
					}
				}
			}
		}
		
		return myArray;
	}


	
public int[] insertionSortBasic(int[] myArray){
		
		int length = myArray.length;
		int temp = 0;
		
		
		for(int i=1; i<length; i++)
		{
			
			if(myArray[i] < myArray[i-1])
			{
				
				for(int j=i; j!=0; j--)
				{
					if(myArray[j] < myArray[j-1])
					{
						temp = myArray[j-1];
						myArray[j-1] = myArray[j];
						myArray[j] = temp;						
					}
					else
					{
						break;
					}
				}
			}
		}
		
		return myArray;
	}

	





public int[] insertionSortBinary(int[] myArray, int graphic){
	
	int length = myArray.length;
	int temp = 0;
	
	if(USE_GRAPHIC)
	{
		sortGraphic.insertionBasicUpdate(0, "blue");
	}
	
	for(int i=1; i<length; i++)
	{
		if(USE_GRAPHIC)
		{
			sortGraphic.insertionBasicUpdate(i, "blue");
			try {
				Thread.sleep(ANIMATION_DELAY);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		findIndexInSortedArray(myArray, 0, i, myArray[i], 1);
		
//		if(USE_GRAPHIC)
//		{
//			sortGraphic.insertionBasicUpdate(foundIndex, "black");
//			try {
//				Thread.sleep(ANIMATION_DELAY);
//			} catch (InterruptedException e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			}
//		}
//		
//		if(USE_GRAPHIC)
//		{
//			sortGraphic.insertionBasicUpdate(foundIndex, "blue");
//		}
		
		if(myArray[i] <= myArray[foundIndex])
		{
			reArrangeValInArray(myArray, i, foundIndex, 1);
		}
		else if(myArray[i] > myArray[foundIndex])
		{
			foundIndex++;
			reArrangeValInArray(myArray, i, foundIndex, 1);
		}
		else if(myArray[i] == myArray[foundIndex] )
		{
			
		}
	}
	
	return myArray;
}





//Returns the index and not the value
public static void findIndexInSortedArray(int[] myArray, int begin, int end, int searchItem, int graphic)
{
	
	if(end == begin)
	{
		foundIndex = end;
		
		return;
	}
	
	int mid = begin + (end - begin)/2;
	
	if(searchItem < myArray[mid])
	{
		if(begin == mid)
		{
			foundIndex = begin;
			return;
		}
		else
		{
			if(USE_GRAPHIC)
			{
				sortGraphic.insertionBasicUpdate(mid, "orange");
				try {
					Thread.sleep(3*ANIMATION_DELAY);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				sortGraphic.insertionBasicUpdate(mid, "blue");
			}
			findIndexInSortedArray(myArray, begin, mid - 1, searchItem, 1);
		}
		
	}
	else if(searchItem > myArray[mid])
	{
		if(mid == end)
		{
			foundIndex = mid;
			return;
		}
		else
		{
			if(USE_GRAPHIC)
			{
				sortGraphic.insertionBasicUpdate(mid, "orange");
				try {
					Thread.sleep(3*ANIMATION_DELAY);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				sortGraphic.insertionBasicUpdate(mid, "blue");
			}
			findIndexInSortedArray(myArray, mid + 1, end, searchItem, 1);
		}
		
	}
	else
	{
		foundIndex = mid;
		return;
	}
	
	return;
	
}


public static int[] reArrangeValInArray(int[] myArray, int indexFrom, int indexTo, int graphic){
	
	int temp = -1;
	int direction = 1;
	if(indexFrom < indexTo)
	{
		direction = -1;
	}
		for(int i = indexFrom; i != indexTo; i=i-1*direction)
		{
			temp = myArray[i-1*direction];
			myArray[i-1*direction] = myArray[i];
			myArray[i] = temp;
			
//			System.out.println(i-1 + ".." + myArray[i-1]);
			if(USE_GRAPHIC)
			{
				
				sortGraphic.insertionBasicUpdate(i-1, myArray[i-1]);
				sortGraphic.insertionBasicUpdate(i, myArray[i]);
				try {
					Thread.sleep(ANIMATION_DELAY);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
			}
			
			
			
		}
	
	
	
	return myArray;
}


public int[] insertionSortBinary(int[] myArray){
	
	int length = myArray.length;
	int temp = 0;
	
	int binaryIndex = -1;
	
	for(int i=1; i<length; i++)
	{
		binaryIndex = returnBinarySearchedIndex(myArray, 0, i-1, myArray[i]);
		reArrangeValInArray(myArray, i, binaryIndex);		
	}
	
	return myArray;
}




//Reimplementation of binary search to retrieve the index in sorted array
public static int returnBinarySearchedIndex(int[] myArray, int begin, int end, int searchItem)
{	
	if(end <= begin)
	{
		return((searchItem < myArray[begin] ? begin : begin + 1));
	}
	int mid = (begin + end)/2;
	
	if(searchItem < myArray[mid])
	{
		return(returnBinarySearchedIndex(myArray, begin, mid - 1, searchItem));	
	}
	else if(searchItem > myArray[mid])
	{
		return(returnBinarySearchedIndex(myArray, mid + 1, end, searchItem));
	}
	else
	{
		return(mid + 1);
	}	
}

public static int[] reArrangeValInArray(int[] myArray, int indexFrom, int indexTo){
	
	int temp = -1;
	int direction = 1;
	if(indexFrom < indexTo)
	{
		direction = -1;
	}
		for(int i = indexFrom; i != indexTo; i=i-1*direction)
		{
			temp = myArray[i-1*direction];
			myArray[i-1*direction] = myArray[i];
			myArray[i] = temp;
		}
	
	
	
	return myArray;
}


}