#include <stdio.h>

int main(void) {
	int length_array;
	int length_subsequence;
	printf("Enter length of the array: ");
	scanf("%d", &length_array);
	printf("Enter length of the subsequence: ");
	scanf("%d", &length_subsequence);
	int array[length_array];
	int subsequence[length_subsequence];
	printf("Enter integers numbers of the array: \n");
	for (int i = 0; i < length_array; ++i) {
		scanf("%d", &array[i]);
	}
	printf("Enter integers numbers of the subsequence: \n");
	for (int i = 0; i < length_subsequence; ++i) {
		scanf("%d", &subsequence[i]);
	}
	int indx = 0;
	int indx1 = 0;
	while (indx < length_array && indx1 < length_subsequence) {
		if (subsequence[indx1] == array[indx]) {
			++indx1;
		}
		++indx;
	}
	if (indx1 == length_subsequence) {
		printf("True\n");
	} else {
		printf("False\n");
	} 
	return 0;
}
