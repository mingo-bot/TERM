class Piece:
    def __init__(self, color, position, symbol):
        self.color = color # 말의 색
        self.position = position # 말의 위치
        self.symbol = symbol # 기호 (e.g., ♟)
    
    def get_moves(self, board):
        raise NotImplementedError # 어미 클래스 말고 자식 클래스에서 구현

class Pawn(Piece): # 앞으로 한 칸, 첫 이동 시 두 칸도 가능, 대각선 잡기 (아직 미완성)
    def get_moves(self, board):
        moves = []
        row, col = self.position
        direction = -1 if self.color == "white" else 1
        # 앞으로 한 칸
        next_move = row + direction 
        if 0 <= next_move < 8 and board.grid[next_move][col] is None:
            moves.append((next_move, col))
            # 앞으로 두 칸
            start_move = 6 if self.color == "white" else 1
            if row == start_move:
                two_move = row + 2 * direction
                if board.grid[two_move][col] is None:
                    moves.append((two_move, col))
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

        self.grid[6] = [Pawn("white", (6, i), "♙") for i in range(8)] # 백
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

    # 체스판 출력    
    def print_board(self):
        for r in range(8):
            row = []
            for c in range(8):
                piece = self.grid[r][c]
                row.append(piece.symbol if piece else "·")
            print(8 - r, " ".join(row))
        print("  a b c d e f g h")



# 메인 실행 함수 정의
def main():
    board = Board() # Board 클래스로부터 체스판 객체를 만들어 board 변수에 담음
    board.print_board() # 체스판 출력

    # 실험 출력용
    pawn = board.grid[6][4]  # e2에 있는 백 폰
    print("e2 폰 이동 가능:", pawn.get_moves(board))  

# 프로그램 시작
main()
