def searchInsert(nums, target):
    left, right = 0, len(nums) - 1 # Khởi tạo chỉ số bên trái và bên phải của phạm vi tìm kiếm
    
    while left <= right: # Vòng lặp tìm kiếm nhị phân
        mid = (left + right) // 2 # Tìm chỉ số giữa của phạm vi tìm kiếm
        
        if nums[mid] == target: # Nếu target được tìm thấy
            return mid # Trả về chỉ mục của target
        
        elif nums[mid] < target: # Nếu target lớn hơn giá trị ở vị trí giữa
            left = mid + 1 # Di chuyển phạm vi tìm kiếm sang phải
            
        else: # Nếu target nhỏ hơn giá trị ở vị trí giữa
            right = mid - 1 # Di chuyển phạm vi tìm kiếm sang trái
            
    return left # Trả về vị trí mà target có thể được chèn vào mảng nums sao cho vẫn duy trì thứ tự tăng dần

# Nhập mảng nums và target
nums = list(map(int, input("Nhap mang nums: ").split()))
target = int(input("Nhap target: "))

# Gọi hàm searchInsert để tìm vị trí hoặc chỉ số của target trong mảng nums
result = searchInsert(nums, target)

print("Vi tri hoac chi so cua target trong mang nums la: ", result)