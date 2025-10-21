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
        row, col = self.position # 현재 위치
        direction = -1 if self.color == "white" else 1 # 전진 방향
        # 앞으로 한 칸
        next_move = row + direction # 이동했을 때의 행 좌표
        if 0 <= next_move < 8 and board.grid[next_move][col] is None: 
            moves.append((next_move, col))
            # 앞으로 두 칸
            start_move = 6 if self.color == "white" else 1 # 폰이 처음 배치되는 행
            if row == start_move: # 행이 시작 위치와 같을 때만 허용
                two_move = row + 2 * direction # direction은 백이면 -1, 흑이면 1
                if board.grid[two_move][col] is None:
                    moves.append((two_move, col))
        # 대각선
        for delta_col in [-1, 1]: # delta_col은 열의 변화량
            diagonal_row, diagonal_col = row + direction, col + delta_col # 대각선 한 칸 앞 좌표
            if 0 <= diagonal_row < 8 and 0 <= diagonal_col < 8:
                target = board.grid[diagonal_row][diagonal_col] # 대각선 칸에 있는 말 정보
                if target and target.color != self.color:
                    moves.append((diagonal_row, diagonal_col))
        return moves
    
class Rook(Piece):
    def get_moves(self, board):
        moves = []
        row, col = self.position # 현재 룩 위치
        directions = [
            (-1, 0), # ↑
            (1, 0), # ↓
            (0, -1), # ←
            (0, 1) # →
        ]
        for delta_row, delta_col in directions:
            next_row = row + delta_row # 현재 위치에서 행 이동
            next_col = col + delta_col # 현재 위치에서 열 이동
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                target = board.grid[next_row][next_col] # 이동할 칸에 말 확인
                if target is None: # 빈 칸이면
                    moves.append((next_row, next_col)) # 이동가능
                elif target.color != self.color: # 상대 말이면
                    moves.append((next_row,next_col)) # 잡을 수 있음
                    break
                else: # 같은 색 말이면
                    break
                # 조건이 맞으면 직선 방향으로 한 칸 전진 반복
                next_row += delta_row
                next_col += delta_col
        return moves

class Knight(Piece):
    def get_moves(self, board):
        moves = []
        row, col = self.position # 현재 나이트 위치
        directions = [
            (-2, -1), (-2, 1), # 위로 2칸 + 좌우 1칸
            (-1, -2), (-1, 2), # 위로 1칸 + 좌우 2칸
            (1, -2), (1, 2), # 아래로 1칸 + 좌우 2칸
            (2, -1), (2, 1) # 아래로 2칸 + 좌우 1칸
        ]
        for delta_row, delta_col in directions:
            next_row = row + delta_row
            next_col = col + delta_col
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                target = board.grid[next_row][next_col]
                if target is None:
                    moves.append((next_row,next_col))
                elif target.color != self.color:
                    moves.append((next_row, next_col))
        return moves

class Bishop(Piece):
    def get_moves(self, board):
        moves = []
        row, col = self.position  # 현재 비숍 위치
        directions = [
            (-1, -1), # ↖ 
            (-1, 1), # ↗ 
            (1, -1), # ↙
            (1, 1) # ↘ 
        ]
        for delta_row, delta_col in directions:
            next_row = row + delta_row
            next_col = col + delta_col

            # 체스판 범위 안에서 계속 전진
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                target = board.grid[next_row][next_col]
                if target is None: # 빈 칸이면 
                    moves.append((next_row, next_col))
                elif target.color != self.color: # 상대 말이면
                    moves.append((next_row, next_col))
                    break  
                else: # 같은 색 말이면 막혀서 이동 불가
                    break
                # 조건이 맞으면 한 칸 전진 반복
                next_row += delta_row
                next_col += delta_col
        return moves
    
class Queen(Piece):
    def get_moves(self, board):
        moves = []
        row, col = self.position  # 현재 퀸 위치
        directions = [
            (-1, 0), # ↑ 
            (1, 0), # ↓ 
            (0, -1), # ← 
            (0, 1), # → 
            (-1, -1), # ↖
            (-1, 1), # ↗ 
            (1, -1), # ↙ 
            (1, 1) # ↘ 
        ]
        for delta_row, delta_col in directions:
            next_row = row + delta_row
            next_col = col + delta_col
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                target = board.grid[next_row][next_col]
                if target is None: # 빈 칸이면
                    moves.append((next_row, next_col))
                elif target.color != self.color: # 상대 말이면 
                    moves.append((next_row, next_col))
                    break
                else: # 같은 색 말이면 막혀서 이동 불가
                    break
                # 조건이 맞으면 한 칸 전진 반복
                next_row += delta_row
                next_col += delta_col
        return moves 

class King(Piece):
    def get_moves(self, board):
        moves = []
        row, col = self.position  # 현재 킹 위치

        # 킹의 8가지 이동 방향 (상하좌우 + 대각선)
        directions = [
            (-1, 0),  # ↑ 위
            (1, 0),   # ↓ 아래
            (0, -1),  # ← 왼쪽
            (0, 1),   # → 오른쪽
            (-1, -1), # ↖ 위-왼쪽
            (-1, 1),  # ↗ 위-오른쪽
            (1, -1),  # ↙ 아래-왼쪽
            (1, 1)    # ↘ 아래-오른쪽
        ]
        for delta_row, delta_col in directions:
            next_row = row + delta_row
            next_col = col + delta_col
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                target = board.grid[next_row][next_col]
                if target is None: # 빈 칸이면 이동 가능
                    moves.append((next_row, next_col))
                elif target.color != self.color: # 상대 말이면 잡을 수 있음
                    moves.append((next_row, next_col))
                # 같은 색 말이면 이동 불가
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
    pawn = board.grid[6][0] # a2에 있는 백 폰
    print("a2 폰 이동 가능:", pawn.get_moves(board))  
    rook = board.grid[7][0] # a1에 있는 백 룩
    print("a1 룩 이동 가능:", rook.get_moves(board))
    knight = board.grid[7][1] # b1에 있는 백 나이트
    print("b1 나이트 이동 가능:", knight.get_moves(board))
    bishop = board.grid[7][2] # c1에 있는 백 비숍
    print("c1 비숍 이동 가능:", bishop.get_moves(board))
    queen = board.grid[7][3] # d1에 있는 백 퀸
    print("d1 퀸 이동 가능:", queen.get_moves(board))   
    king = board.grid[7][4] # e1에 있는 백 나이트
    print("e1 킹 이동 가능:", king.get_moves(board))
# 프로그램 시작
main()
