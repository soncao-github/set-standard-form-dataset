import os
import glob

# Đếm số lượng file (dùng để kiểm tra xem 2 folder chứa số file bằng nhau hay không để ghép lại)
def count_file_check(folder_path):
    txt_files = glob.glob(folder_path + '/*.txt')
    count_file = len(txt_files)
    print("Số lượng file .txt trong thư mục", folder_path, "là:", count_file)

# Ghép nội dung file txt cho YOLO
def insert_contents(target_file, contents_file, path_new_file, count_new_file):
    # Mở file, thêm khoảng trắng phía sau file cần chèn (file targer) => tạo form chuẩn cho dataset của YOLO
    with open(target_file, 'r') as target:
        target_content = target.read()

    target_content = target_content + " "
    with open(target_file, 'w') as target:
        target.write(target_content)
    
    with open(target_file, 'r') as target:
        target_content = target.read()

    with open(contents_file, 'r') as contents:
        contents_data = contents.read()

    # Tìm vị trí khoảng trắng thứ 7 và các khoảng trắng sau mỗi 2 khoảng trắng
    positions = []
    count = 0
    for i, char in enumerate(target_content):
        if char == ' ':
            count += 1
            if count == 7 or (count > 7 and (count - 7) % 2 == 0):
                positions.append(i)

    # Kiểm tra xem số lượng nội dung có thể chèn có đủ để chèn vào các vị trí khoảng trắng
    if len(contents_data) < len(positions):
        print(f"Số lượng nội dung chèn không đủ tại file {count_new_file + 1}")
        return

    # Chèn nội dung vào các vị trí khoảng trắng
    updated_content = target_content
    pos = 0  
    for i in range(len(positions)):
        position = positions[i]
        content_data = contents_data[i]
        updated_content = updated_content[:(position + pos)] + " " + content_data + updated_content[(position + pos):]
        pos += 2    # Mỗi lần chèn nội dung bị dời đi 2 kí tự
    
    # Tạo file mới đã xử lý vào đường dẫn khác
    new_file_name = f'{count_new_file + 1}.txt'
    nf_path = path_new_file + '/' + new_file_name
    with open(nf_path, 'w') as new:
        new.write(updated_content)
    
    # Bỏ đi khoảng trắng phía trên đã thêm vào để nội dung file về ban đầu
    target_content = target_content.rstrip()
    with open(target_file, 'w') as target:
        target.write(target_content)

# Gán path tùy vào máy tính
def main():
    for k in range(500): # Số range = số lượng file đếm được ở folder (cả 2 folder phải có số file như nhau)
        target_file = f'C:/Users/HOASON/Desktop/dataset500/txt/{k+1}.txt'
        contents_file = f'C:/Users/HOASON/Desktop/dataset500/keypoint/split/split {k+1}.txt'
        path_new_file = f'C:/Users/HOASON/Desktop/dataset500/new'
        insert_contents(target_file, contents_file, path_new_file, k)
    print('Complete!!!')

# Thay đổi đường dẫn tới thư mục cần kiểm tra
# folder_path = 'C:/Users/HOASON/Desktop/dataset500/txt'
folder_path = 'C:/Users/HOASON/Desktop/dataset500/keypoint/split'

# Chạy chương trình
count_file_check(folder_path)
# main()

