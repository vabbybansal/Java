package sorts;

public class heapSort{
	
	static public int[] myArray = {6,4,10,14,99,7,9,3,999,999,0,2,999,8,1,20};
	
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

	public int[] myHeapSort(int[] myArray)
	{
		int arrayLength = myArray.length;
		int heapSize = arrayLength;
		
		int[] heapedArray = new int[myArray.length];
		int temp;
		
		for(int i = 0; i < arrayLength; i++)
		{
			//Find max of heap and put in heapedArray(sorted array)
			heapedArray[i] = buildMaxHeap(myArray, heapSize)[0];
			
			//Swap the highest element with the end of the logical heap. It will not be used from now on so that the next max elements are extracted from the heap
			temp = myArray[0];
			myArray[0] = myArray[heapSize-1];
			myArray[heapSize-1] = temp;
			heapSize--;
		}
		
		return heapedArray;
	}
	
	public int[] buildMaxHeap(int[] myArray, int logicalArrayLength){
		
		int len = (logicalArrayLength != -1) ? logicalArrayLength : myArray.length;
		
		//indexes in this function matches conceptual model of heap where index starts from 1
		//thus, whenever the elements are to be accessed from the array, index will be decremented by 1

		//Run maxHeapify for non leafy nodes, bottom-up
		//Leaves start from (n/2+1); so run for elements before that, i.e., n/2
		for(int index = len/2; index != 0; index--)
		{
			//increment the index population of array, to meet the conceptual logic of the heap, whose index starts from 1
			myArray = maxHeapify(myArray, index, logicalArrayLength);
		
		}
			
		return myArray;
	}
	
	public int[] maxHeapify(int[] myArray, int rootIndex, int logicalArrayLength){
		
		//All indexes in maxHeapify are acc to the conceptual model of heap where indexe of root starts from 1
		//rootIndex in this function came from builMaxHeap function incremented by 1, to match the conceptual model of heap
		
		int len = (logicalArrayLength != -1) ? logicalArrayLength : myArray.length;
		
		//Base condition of recurrence to stop maxHeapify at the leaf (rootIndex->leaf)		
		// Leaf Node = len/2 + 1;
		int leafNode = len/2 + 1; 
		if(rootIndex >= leafNode)
		{
			return myArray;
		}
		
		//leftChild and rightChild values below in concptual logic of heap
		int leftChild = 2*rootIndex;
		int rightChild = leftChild + 1;
		int max;
		int temp;
		
		//Check if left child is larger than the root index, put value in max
		//NOTE: for all comparisons on array, actual values instead of the conceptual level will work, so bring down all indexes by 1
		max = (myArray[leftChild - 1] > myArray[rootIndex - 1]) ? leftChild : rootIndex;
		
		//Compare to max of root and leftChild, if right exists
		if(rightChild <= len)
		{
			if(myArray[rightChild - 1] > myArray[max - 1])
			{
				max = rightChild;
			}
		}
		
		//Swap the root is smaller than any child, swap the root with the biggest child
		if(max != rootIndex)
		{
			temp = myArray[rootIndex - 1];
			myArray[rootIndex - 1] = myArray[max - 1];
			myArray[max -1] = temp;
			return maxHeapify(myArray, max, logicalArrayLength);
		}
		else
		{
			return myArray;
		}
		
		
	}
	
	
}



