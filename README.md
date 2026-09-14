# Bài thực hành Git, Python và NumPy

## Tư liệu dùng để nộp

- `report/index.html`: mở bằng trình duyệt để đọc báo cáo.
- `report/all_python.html`: toàn bộ 112 ô mã cùng đầu ra thực tế.
- `python_tutorial.py`: mã Python độc lập, đã chạy kiểm tra.
- `python_results.txt`, `git_results.txt`, `remote_verified.json`: nhật ký và bằng chứng kiểm tra.
- `GitTutorial.bundle`: bản sao đầy đủ lịch sử Git, có thể clone lại.

Git được thực hiện bằng CLI. Các commit ghi tác giả `Tutorial Automation <tutorial@example.invalid>` để thể hiện rõ đây là thao tác tự động, không giả danh danh tính cá nhân của sinh viên.

## Kết quả Git

Repository: https://github.com/pthaianh2006-rgb/BME-MACHINE-LEARNING

- `master`: tmp.txt có dòng `Hello MLH course!`.
- `example`: tmp.txt có thêm dòng `This is an example`.
- `example2`: đã merge example, có tmp.txt hai dòng và tmp2.txt rỗng.
- Đã clone, add, commit, checkout phiên bản ban đầu, tạo nhánh, merge và push ba nhánh; hash remote đã đối chiếu với local.
- Khi checkout initial commit, tmp.txt biến mất; README.md và .gitignore vẫn còn.
- Trước add: file untracked; sau add: một file staged. Commit lưu phiên bản local; push mới đưa commit lên remote.

Không thực hiện GitHub Classroom của khóa học gốc vì sử dụng repository cá nhân do bạn cung cấp. Không cài/chụp Sourcetree; dùng thao tác Git CLI tương đương. Thứ tự push diễn ra sau các thao tác local do cần hoàn tất đăng nhập.

## Kết quả Python

Chạy thành công 112 ô mã bằng Python 3.12.14 và NumPy 2.3.5; kiểm tra ba kết quả quan trọng bằng assertion. Mã Python độc lập cũng được chạy lại thành công.

- Câu hỏi cell 72: `[0, 1, 2, 1]`.
- Câu hỏi cell 116: `[0, 1, 1, 2, 3, 6, 8]`.
- Các thông báo `'monkey'` và thiếu đối số `a3` là minh họa lỗi đã được try/except bắt trong mã gốc.
- Bỏ CSS dành riêng cho notebook; thay `np.int` đã bị loại bỏ bằng `int`; hiển thị biểu thức cuối qua `_show`; seed ngẫu nhiên 42.
- Dùng Python có sẵn. Chưa tạo môi trường Conda/chạy Jupyter. `environment.yml` là cấu hình tùy chọn để tự tạo môi trường, không phải bằng chứng đã cài.

Chạy lại: `python python_tutorial.py` (cần NumPy theo requirements.txt).
Để chạy lại kèm nhật ký có cấu trúc: `python run_python.py`.
Không chạy lại `run_git.py` trên repository đã có bài: script này dành cho bản clone trống ban đầu.

## Nguồn

- https://github.com/aim-lab/mlh-course-material/tree/master/tutorials/BME-336546-C00-Introduction%20to%20Git
- https://github.com/aim-lab/mlh-course-material/tree/master/tutorials/BME-336546-C01-Python%2C%20numpy%20and%20friends

Nguồn notebook GitHub được lưu dưới dạng JSON chỉ để đọc. Không chỉnh sửa hoặc tạo file .ipynb của người dùng.
