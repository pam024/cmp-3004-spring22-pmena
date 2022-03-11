#include <stdio.h>
#include <stdlib.h>

int abs_diff(int a, int b){
	int diff;
	
	if(a > b){
		diff = abs(a-b); 
		printf("Absolute value: %d \n", diff);
	}else{
		diff = abs(b-a);
		printf("Absolute value: %d \n", diff);
	}
	
	return diff;	
}

int main(){
	int num1, num2;
	printf("Enter two integers numbers: \n");
	scanf("%d", &num1);
	scanf("%d", &num2);
	
	abs_diff(num1, num2);
	
	return 0;
}



