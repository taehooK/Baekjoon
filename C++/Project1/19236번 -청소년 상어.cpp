#include <cstdio>
#include <vector>
#include <cassert>
#include <string>
#define N 4

typedef struct coordinate
{
	int x;
	int y;
}Coordinate;


class Fish
{
public:
	Fish() = default;
	Fish(int number, bool isLive, int row, int column, int direction);
	Coordinate GetNextMove();
	void Move(int row, int column);
	void Rotate();

public:
	int number;
	bool isLive;
	int row;
	int column;
	int direction;
};

Fish::Fish(int number, bool isLive, int row, int column, int direction)
{
	this->number = number;
	this->isLive = isLive;
	this->row = row;
	this->column = column;
	this->direction = direction;
}

int dy[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dx[8] = { 0, -1, -1, -1, 0, 1, 1, 1 };

Coordinate Fish::GetNextMove()
{
	Coordinate coordinate;
	coordinate.y = this->row + dy[this->direction];
	coordinate.x = this->column + dx[this->direction];
	
	return coordinate;
}
void Fish::Move(int row, int column)
{
	this->row = row;
	this->column = column;
}
void Fish::Rotate()
{
	this->direction++;
	if (this->direction >= 8)
	{
		this->direction = 0;
	}
}

using namespace std;

int maxSum;

bool isMovableForFish(Fish board[N][N], Coordinate coordinate)
{
	int y = coordinate.y;
	int x = coordinate.x;
	
	if (0 <= y && y < N && 0 <= x && x < N &&
		(board[y][x].number == 0 ||
		board[y][x].number > 0)) // 빈칸이거나 물고기이면 통과
	{

		return true;
	}
	return false;
}

bool isMovableForShark(Fish board[N][N], Coordinate coordinate)
{
	int y = coordinate.y;
	int x = coordinate.x;
	if (0 <= y && y < N &&
		0 <= x && x < N ) 
	{
		return true;
	}
	return false;
}

void move_fishes(Fish board[N][N], vector<Fish>* fishes)
{
	//0. 물고기들을 이동시킨다. 1번부터~16번까지
	for (auto it = (*fishes).begin(); it != (*fishes).end(); ++it)
	{
		Fish* fish = &*it;

		if (fish->isLive == false)
		{
			continue;
		}

		Coordinate next_move = fish->GetNextMove();
		// 이동할 수 있으면
		if (!isMovableForFish(board, next_move))
		{
			fish->Rotate();
			next_move = fish->GetNextMove();
			while (isMovableForFish(board, next_move) == false)
			{
				fish->Rotate();
				next_move = fish->GetNextMove();
			}
		}
		
		Fish to = board[next_move.y][next_move.x];
		board[next_move.y][next_move.x] = *fish;
		board[fish->row][fish->column] = to;

		if (to.number > 0)
		{
			(*fishes)[to.number - 1].Move(fish->row, fish->column);
		}
		board[next_move.y][next_move.x].Move(next_move.y, next_move.x);
		board[fish->row][fish->column].Move(fish->row, fish->column);
		fish->Move(next_move.y, next_move.x);
		
	}
}

void copyBoard(Fish dest[N][N], Fish source[N][N])
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			dest[i][j] = source[i][j];
		}
	}
}


void dfs(Fish board[N][N], vector<Fish> fishes, Fish shark, int sum)
{
	move_fishes(board, &fishes);
	Coordinate next = shark.GetNextMove();
	board[shark.row][shark.column].number = 0;

	while (isMovableForShark(board, next) == true)
	{
		shark.Move(next.y, next.x);
		
		if (board[next.y][next.x].number > 0)
		{
			Fish copiedBoard[N][N];
			copyBoard(copiedBoard, board);

			Fish eattenFish = copiedBoard[next.y][next.x];
			copiedBoard[next.y][next.x].number = -1;
			fishes[eattenFish.number - 1].isLive = false;
			
			dfs(copiedBoard, fishes, copiedBoard[next.y][next.x], sum + eattenFish.number);
			fishes[eattenFish.number - 1].isLive = true;
		}

		next = shark.GetNextMove();
	}
	
	if (sum > maxSum)
	{
		maxSum = sum;
	}
}


void inputAndSet(vector<Fish>* fishes, Fish board[N][N])
{
	int numbers[N];
	int directs[N];
	int row = 0;
	for (int i = 0; i < N; i++)
	{
		int column = 0;
		scanf("%d %d %d %d %d %d %d %d", &numbers[0], &directs[0], &numbers[1], &directs[1], &numbers[2], &directs[2], &numbers[3], &directs[3]);
		for (int j = 0; j < N; j++)
		{
			int number = numbers[j];
			int direct = directs[j];
			Fish fish = Fish(number, true, row, column, direct - 1);
			board[row][column] = fish;

			(*fishes)[number - 1] = fish;
			column++;
		}
		row++;
	}
}

int main() {
	vector<Fish> fishes;
	int n = N;
	Fish board[N][N];
	for (int i = 0; i < 16; i++)
	{
		Fish fish;
		fishes.push_back(fish);
	}// 물고기들 미리 셋팅

	inputAndSet(&fishes, board);// 입력받는다.

	
	int sum = board[0][0].number;
	
	; //상어 번호 -1
	fishes[board[0][0].number - 1].isLive = false;
	board[0][0].number = -1;
	

	dfs(board, fishes, board[0][0], sum);

	printf("%d\n", maxSum);
	
}