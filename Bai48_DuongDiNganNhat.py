import heapq

def min_steps_to_reach_end(n, m, matrix):
    # Khởi tạo bảng dp với giá trị vô cùng (infinity) và bảng đếm số bước
    dp = [[float('inf')] * m for _ in range(n)]
    step_count = [[float('inf')] * m for _ in range(n)]  # Bảng đếm số bước
    dp[0][0] = 0  # Chi phí bắt đầu là 0
    step_count[0][0] = 0  # Số bước di chuyển bắt đầu là 0

    # Hàng đợi ưu tiên (min-heap)
    pq = [(0, 0, 0)]  # (chi phí, x, y) => bắt đầu từ (0, 0) với chi phí 0

    # Các hướng di chuyển: xuống dưới, sang phải, chéo xuống
    directions = [(1, 0), (0, 1), (1, 1)]  # (di chuyển xuống, sang phải, chéo xuống)

    while pq:
        cost, x, y = heapq.heappop(pq)  # Lấy phần tử có chi phí thấp nhất

        # Nếu chi phí hiện tại đã lớn hơn chi phí đã lưu, bỏ qua
        if cost > dp[x][y]:
            continue

        # Duyệt qua các hướng di chuyển
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # Tính chi phí di chuyển
                new_cost = cost + abs(matrix[x][y] - matrix[nx][ny])
                new_steps = step_count[x][y] + 1  # Cập nhật số bước di chuyển

                # Nếu tìm thấy đường đi với chi phí thấp hơn, hoặc cùng chi phí nhưng ít bước hơn
                if new_cost < dp[nx][ny]:
                    dp[nx][ny] = new_cost
                    step_count[nx][ny] = new_steps
                    heapq.heappush(pq, (new_cost, nx, ny))
                elif new_cost == dp[nx][ny] and new_steps < step_count[nx][ny]:
                    step_count[nx][ny] = new_steps
                    heapq.heappush(pq, (new_cost, nx, ny))

    # Nếu không thể đến đích, trả về -1, ngược lại trả về chi phí và số bước
    if dp[n - 1][m - 1] == float('inf'):
        return -1, -1  # Không thể đến đích
    return dp[n - 1][m - 1], step_count[n - 1][m - 1]  # Trả về chi phí và số bước di chuyển


def main():
    t = int(input())  # Đọc số lượng test case
    for _ in range(t):
        n, m = map(int, input().split())  # Đọc kích thước ma trận
        matrix = []
        for i in range(n):
            row = list(map(int, input().split()))  # Đọc từng dòng của ma trận
            matrix.append(row)
        
        # Tính số bước ít nhất và in ra kết quả
        cost, steps = min_steps_to_reach_end(n, m, matrix)
        print(steps + 1)  # In ra chi phí và số bước di chuyển


if __name__ == "__main__":
    main()
