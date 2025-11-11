import sys

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
        self.current_turn = "white" # 게임 시작은 백부터

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

    def to_chess_notation(self, row, col): # 체스 표기법으로 변환
        eng = "abcdefgh"
        num = "87654321"
        return eng[col] + num[row]
    
    def from_chess_notation(self, square): # 체스 표기법에서 변환
        eng = "abcdefgh"
        num = "87654321"
        col = eng.index(square[0])
        row = num.index(square[1])
        return (row, col)

    # 체스판 출력    
    def print_board(self):
        for r in range(8):
            row = []
            for c in range(8):
                piece = self.grid[r][c]
                row.append(piece.symbol if piece else "·")
            print(8 - r, " ".join(row))
        print("  a b c d e f g h")

    def find_king(self, color): # 턴 마다 킹의 위치를 찾아 반환
        for r in range(8):
            for c in range(8):
                piece = self.grid[r][c]
                if piece and isinstance(piece, King) and piece.color == color:
                    return (r, c)
        return None # 킹이 없으면 None (게임 종료)

    def in_check(self, color): # 자신의 킹이 공격받고 있는지 확인
        king_position = self.find_king(color)
        if not king_position:
            return False  # 킹이 없으면 False (게임 종료)
        
        opponent_color = "black" if color == "white" else "white" # 상대 색상 결정
       
        # 상대 말들의 이동 가능 칸 확인
        for r in range(8):
            for c in range(8):
                piece = self.grid[r][c]
                if piece and piece.color == opponent_color:
                    moves = piece.get_moves(self) # 상대 말의 이동 가능 위치
                    if king_position in moves:
                        return True
        return False

# 체크메이트 확인
    def is_checkmate(self, color):
        if not self.in_check(color): # 체크 상태가 아니면 체크메이트도 아님
            return False

        # 해당 색 모든 말의 이동을 시도 (킹을 지킬 수 있는지)
        for r in range(8):
            for c in range(8):
                piece = self.grid[r][c]
                if piece and piece.color == color: 
                    for move in piece.get_moves(self):
                        # 가상 이동 시도 (체스판에 반영X)
                        backup_piece = self.grid[move[0]][move[1]]
                        original_pos = piece.position 
                        self.grid[move[0]][move[1]] = piece 
                        self.grid[r][c] = None 
                        piece.position = move

                        still_in_check = self.in_check(color) # 이동 후에도 체크 상태인지 확인

                        # 이동 되돌리기
                        self.grid[r][c] = piece
                        self.grid[move[0]][move[1]] = backup_piece
                        piece.position = original_pos

                        # 체크에서 벗어날 수 있는 수가 있으면 체크메이트 아님
                        if not still_in_check:
                            return False
                        
        return True # 모든 수가 체크 상태라면 체크메이트

    def move_piece(self, start: str, end: str): #말 이동 함수
        start_row, start_col = self.from_chess_notation(start)
        end_row, end_col = self.from_chess_notation(end)

        piece = self.grid[start_row][start_col] # 시작 위치에 있는 말
        if piece is None: 
            print("해당 위치에 말이 없습니다.")
            return False
        
        # 턴 확인
        if piece.color != self.current_turn:
            print(f"지금은 {self.current_turn} 차례입니다. {piece.color} 말은 움직일 수 없습니다.")
            return False

        # 이동 가능한 좌표 목록 가져오기
        possible_moves = piece.get_moves(self) 
        if (end_row, end_col) not in possible_moves:
            print("해당 위치로 이동할 수 없습니다.")
            return False
        target = self.grid[end_row][end_col] # 도착 위치에 있는 말
        if target:
            print(f"{target.color} { target.__class__.__name__}을 잡았습니다.")
        
        # 실제 이동 처리
        self.grid[end_row][end_col] = piece # 도착 위치에 말 배치
        self.grid[start_row][start_col] = None # 원래 자리 비우기
        piece.position = (end_row, end_col) # 말의 위치 정보 업데이트
        
        print(f"{piece.color} {piece.__class__.__name__}이(가) "f"{start} → {end} 로 이동했습니다.")
        self.print_board()

        # 턴 교체
        self.current_turn = "black" if self.current_turn == "white" else "white"
        print(f"다음 턴: {self.current_turn}")

        # 체크/체크메이트 판정
        if self.in_check(self.current_turn):
            if self.is_checkmate(self.current_turn):
                print(f"{self.current_turn} 킹이 체크메이트 당했습니다! 게임 종료!")
                sys.exit() 
            else:
                print(f"{self.current_turn} 킹이 체크 상태입니다!")

        return True

# 메인 실행 함수 정의
def main():
    board = Board() # Board 클래스로부터 체스판 객체를 만들어 board 변수에 담음
    board.move_piece("e2", "e4")
    board.move_piece("e7", "e5")
    board.move_piece("d1", "h5")
    board.move_piece("b8", "c6")
    board.move_piece("f1", "c4")
    board.move_piece("g8", "f6")
    board.move_piece("h5", "f7")

# 프로그램 시작
main()
