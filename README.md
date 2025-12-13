# 🍎 Fruit Catcher - Game Hứng Trái Cây

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Pygame-Game%20Engine-red)
![Status](https://img.shields.io/badge/Status-Completed-green)

> **Đồ án môn học:** Nhập môn ngành Kỹ thuật Máy tính  
> **Trường:** Đại học Bách khoa - Đại học Đà Nẵng (DUT)  
> **Tác giả:** DUTVcore & TranHuuLai

## 📖 Giới thiệu

**Fruit Catcher** là một trò chơi giải trí vui nhộn được xây dựng bằng ngôn ngữ Python và thư viện Pygame. Người chơi sẽ điều khiển một chiếc xô để hứng các loại trái cây rơi xuống, tích lũy điểm số và sinh tồn qua các cấp độ khó tăng dần.

Dự án này minh họa cách xử lý va chạm (collision detection), quản lý trạng thái game (state management), đóng gói phần mềm (PyInstaller) và xử lý logic game theo hướng đối tượng.

## 🚀 Tính năng nổi bật

Dựa trên mã nguồn hiện tại, game bao gồm các tính năng:

* **Hệ thống 4 Mùa:** Hình nền thay đổi theo điểm số (Xuân, Hạ, Thu, Đông) tạo cảm giác mới mẻ.
* **Vật phẩm đa dạng:**
    * 🍌 **Chuối:** Hồi phục 1 mạng (tối đa 5 mạng).
    * 🍎 **Táo:** Kích hoạt **Khiên bảo vệ** trong 3 giây (chống bom).
    * 🍉 **Dưa hấu / Dâu tây:** Cộng điểm thưởng.
    * 💣 **Bom:** Trừ mạng nếu hứng phải (trừ khi đang có khiên).
* **Hiệu ứng sinh động:** Hiệu ứng chữ bay (Floating Text) khi ăn điểm hoặc dính bom, vòng tròn bảo vệ khi có khiên.
* **Độ khó tăng dần:** Tốc độ rơi và tần suất xuất hiện trái cây tăng lên theo cấp độ (Level).
* **Âm thanh:** Nhạc nền và hiệu ứng âm thanh cho từng hành động (ăn điểm, nổ bom, game over).

## 🛠️ Công nghệ sử dụng

* **Ngôn ngữ:** Python
* **Thư viện chính:** Pygame (Xử lý đồ họa và âm thanh)
* **Công cụ đóng gói:** PyInstaller (Tạo file .exe để chạy không cần cài Python)

## ⚙️ Cài đặt và Chạy game

### Cách 1: Chạy từ mã nguồn (Source Code)

1.  **Clone repository:**
    ```bash
    git clone [https://github.com/DUTVcore/Game_baitapnhapmonnganh.git](https://github.com/DUTVcore/Game_baitapnhapmonnganh.git)
    cd Game_baitapnhapmonnganh
    ```

2.  **Cài đặt thư viện:**
    Yêu cầu máy đã cài Python. Chạy lệnh sau để cài `pygame`:
    ```bash
    pip install pygame
    ```

3.  **Chạy game:**
    ```bash
    python game.py
    ```

### Cách 2: Chạy file EXE (Windows)

Nếu bạn đã build hoặc tải bản release, chỉ cần mở file `game.exe` trong thư mục `dist` để chơi ngay mà không cần cài đặt Python.

*(Để tự build file exe từ source, chạy lệnh: `pyinstaller game.spec`)*

## 🎮 Hướng dẫn chơi

* **Di chuyển:** Sử dụng phím mũi tên **TRÁI** (⬅️) và **PHẢI** (➡️) để di chuyển xô.
* **Mục tiêu:**
    * Hứng trái cây để ghi điểm.
    * Tránh né bom (nếu chạm bom sẽ mất 1 mạng).
    * Đừng để trái cây rơi xuống đất (sẽ bị mất mạng).
* **Game Over:** Trò chơi kết thúc khi bạn mất hết 3 mạng (hoặc 5 mạng nếu đã ăn chuối).

## 📂 Cấu trúc thư mục

```text
Game_baitapnhapmonnganh/
├── imgs/               # Chứa hình ảnh (background, trái cây, icon)
├── sounds/             # Chứa nhạc nền và hiệu ứng âm thanh
├── game.py             # Mã nguồn chính của trò chơi
├── settings.py         # File cấu hình (kích thước màn hình, màu sắc, đường dẫn)
├── game.spec           # File cấu hình cho PyInstaller
└── README.md           # Tài liệu hướng dẫn
