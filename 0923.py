class Piece:
    def __init__(self, color, position, symbol):
        self.color = color # 말의 색
        self.position = position # 말의 위치
        self.symbol = symbol # 기호 (e.g., ♟)
    
    def get_moves(self, board):
        raise NotImplementedError # 어미 클래스 말고 자식 클래스에서 구현

class Pawn(Piece):
    def get_moves(self, board):
        moves = []
        # 앞으로 한 칸, 첫 시작시 두 칸도 가능, 대각선 잡기 (아직 미구현)
        return moves
    
class Rook(Piece):
    def get_moves(self, board):
        moves = []
        # 상하좌우 직선 (아직 미구현)
        return moves
    
class Knight(Piece):
    def get_moves(self, board):
        moves = []
        # L자 (아직 미구현)
        return moves

class Bishop(Piece):
    def get_moves(self, board):
        moves = []
        # 대각선 (아직 미구현)
        return moves
    
class Queen(Piece):
    def get_moves(self, board):
        moves = []
        # 직선 대각선 (아직 미구현)
        return moves 

class King(Piece):
    def get_moves(self, board):
        moves = []
        # 모든 방향 한 칸씩 (아직 미구현)
        return moves   

# 체스판 클래스
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self): # 흑
        self.grid[0] = [
            Rook("black", (0, 0), "♜"),
            Knight("black", (0, 1), "♞"),
            Bishop("black", (0, 2), "♝"),
            Queen("black", (0, 3), "♛"),
            King("black", (0, 4), "♚"),
            Bishop("black", (0, 5), "♝"),
            Knight("black", (0, 6), "♞"),
            Rook("black", (0, 7), "♜")
        ]
        self.grid[1] = [Pawn("black", (1, i), "♟") for i in range(8)]

        self.grid[6] = [Pawn("white", (6, i), "♙") for i in range(8)]
        self.grid[7] = [
            Rook("white", (7, 0), "♖"),
            Knight("white", (7, 1), "♘"),
            Bishop("white", (7, 2), "♗"),
            Queen("white", (7, 3), "♕"),
            King("white", (7, 4), "♔"),
            Bishop("white", (7, 5), "♗"),
            Knight("white", (7, 6), "♘"),
            Rook("white", (7, 7), "♖")
        ]
        
# 체스판 생성 (업그레이드 중)
def create_board():
    board = [
        ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"], #흑
        ["♟"] * 8,
        ["."] * 8,
        ["."] * 8,
        ["."] * 8,
        ["."] * 8,
        ["♙"] * 8, # 백
        ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"] 
    ]
    return board

# 체스판 출력 + 좌표 (업그레이드 필요)
def print_board(board):
    for i, row in enumerate(board): # i와 행을 동시에 가져옴
        print(8-i, " ".join(row))
    print("  a b c d e f g h")

# 메인 실행 함수 정의
def main():
    board = Board() # Board 클래스로부터 체스판 객체를 만들어 board 변수에 담음
    board = create_board()   # 체스판 생성
    print_board(board)       # 체스판 출력

# 프로그램 시작
main()
