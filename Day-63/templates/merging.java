import java.util.*;

public class merging{
	static void mergeSort(int arr[]){
		int n = arr.length;
		if(n<2)
			return;
		int mid = n/2;
		int left[] = Arrays.copyOfRange(arr, 0, mid);
		mergeSort(left);
		int right[] = Arrays.copyOfRange(arr, mid, n);
		mergeSort(right);
		merge(left, right, arr);
	}
	static void merge(int left[], int right[], int arr[]){
		int pL = 0;
		int pR = 0;
		int index = 0;
		while(pL<left.length && pR<right.length){
			if(left[pL]<right[pR])
				arr[index++] = left[pL++];
			else
				arr[index++] = right[pR++];
		}
		while(pL<left.length)
			arr[index++] = left[pL++];
		while(pR<right.length)	
			arr[index++] = right[pR++];
	}
	static void print(int arr[]){
		int n = arr.length;
		for(int i=0; i<n; i++)
			System.out.print(arr[i]+" ");
	}
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int arr[] = new int[n];
		for(int i=0; i<n; i++)
			arr[i] = sc.nextInt();
		mergeSort(arr);
		print(arr);
	}
}