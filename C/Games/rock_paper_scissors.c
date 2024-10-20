#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define ROCK "rock"
#define SCISSORS "scissors"
#define PAPER "paper"
//return random int between 0 and 2
unsigned short choice() {
	return rand() % 3; 
}

// Handle the user choice
void userChoice(char* user_choice) {
	printf("rock, paper, scissors: ");
	scanf("%8s", user_choice);
	while(getchar() != '\n'); //Clearing the buffer for cases in which the string inserted by the user was too long and the newline character was not read by the scanf.
	while (strcmp(user_choice, ROCK) != 0 && strcmp(user_choice, PAPER) != 0 && strcmp(user_choice, SCISSORS) != 0) {
		printf("You need to choose between rock, paper or scissors: ");
		scanf("%8s", user_choice);
		while(getchar() != '\n');
	}
}

// Genereting the machine choice
void machineChoice(char *machine_choice) {
	unsigned short random_number = choice();
	char *game_options[3] = {ROCK, PAPER, SCISSORS};
	strcpy(machine_choice, game_options[random_number]);
}

// main logic of the game
int rockPaperScissors() {
	char user_choice[9]; 
	char machine_choice[9];					 //
	unsigned short user_points = 0, machine_points = 0;
	while (user_points < 3 && machine_points < 3) {
		userChoice(user_choice);
		machineChoice(machine_choice);
		printf("Your choice: %s\n", user_choice);
		printf("Machine choice: %s\n", machine_choice);
		if (strcmp(user_choice, machine_choice) == 0) {
			printf("Draw!\n");
			printf("User points: %d\nMachine points: %d\n\n", user_points, machine_points);
		} 
		else if ((strcmp(user_choice, ROCK) == 0 && strcmp(machine_choice, SCISSORS) == 0) ||
		(strcmp(user_choice, PAPER) == 0 && strcmp(machine_choice, ROCK) == 0) ||
        (strcmp(user_choice, SCISSORS) == 0 && strcmp(machine_choice, PAPER) == 0)) {
			user_points++;
			printf("You win!\n");
			printf("User points: %d\nMachine points: %d\n\n", user_points, machine_points);
		}
		else {
			machine_points++;
			printf("You lose...\n");
			printf("User points: %d\nMachine points: %d\n\n", user_points, machine_points);
		}
	}
	if (user_points == 3) {
		printf("You won the battle!\n");
	}
	else {
		printf("You lost the battle..\nTry again\n");
	}
	return 0;
	
}

int main() {
	srand(time(NULL)); //Setting the seed for random number generator.
	rockPaperScissors();
	return 0;
}
