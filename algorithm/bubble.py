num = [20, 70, 90, 40, 10]


def bubble(data):
    n = len(data)
    for i in range(n):
      # 有 n 個資料長度，但只要執行 n-1 次
        for j in range(n-i-1):
          # 從第1個開始比較直到最後一個還沒到最終位置的數字
            if data[j] > data[j+1]:        # 比大小然後互換
                data[j], data[j+1] = data[j+1], data[j]
        print(data)


bubble(num)
