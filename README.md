# Data-Fashion-MNIST

## Các mô hình thử nghiệm
### 1. Mô hình Neural Network với chỉ một hidden layer
[![udtgmt.png](https://i.postimg.cc/C1QP6PTb/udtgmt.png)](https://postimg.cc/Hcb9rtLL)
- Ảnh đầu vào có kích thước 28 x 28 được chuyển thành một vector có kích thước 784, được đưa vào input, output gồm 10 node tương ứng với 10 labels dữ liệu. Hidden layer có 128 node, activation là hàm ReLU.
- Kết quả accuracy trên tập train: 93.29%, accuracy trên tập test: 88.93%.
### 2. Mô hình Deep Neural Network (có nhiều hơn 1 hidden layer)
[![udtgmt.png](https://i.postimg.cc/6qzdmTGg/udtgmt.png)](https://postimg.cc/q6hhtJwx)
- Mô hình có 3 hidden layer lần lượt có số node lần lượt là 256, 192, 128 và có thêm 2 lớp Batch Normalization.
- Về Batch Normalization: 
  - Chuẩn hóa các feature (đầu ra của mỗi layer sau khi đi qua các activation) về trạng thái zero-mean với độ lệch chuẩn 1. 
  - Tránh được hiện tượng giá trị tham số rơi vào khoảng bão hòa sau khi đi qua các hàm kích hoạt phi tuyến, đảm bảo rằng không có sự kích hoạt nào bị vượt quá cao hoặc quá thấp, các weights mà khi không dùng BN có thể sẽ không bao giờ được học thì lại được học bình thường nên làm giảm đi sự phụ thuộc vào giá trị khởi tạo của tham số.   
  - Vai trò như một dạng của regularization giúp cho việc giảm overfitting. Sử dụng Batch Normalization, không cần phải sử dụng quá nhiều Dropout và điều này rất có ý nghĩa vì không cần phải lo lắng vì bị mất quá nhiều thông tin khi dropout weights của mạng. Tuy nhiên vẫn nên sử dụng kết hợp cả 2 kĩ thuật này.  
- Kết quả accuracy trên tập train: 97.07%, kết quả accuracy trên tập test: 89.56%.

### 3. Mô hình Convolutional Neural Network
[![udtgmt.png](https://i.postimg.cc/9Mm0NbtX/udtgmt.png)](https://postimg.cc/LqWmJzbG)
[![udtgmt.png](https://i.postimg.cc/2jBy91nZ/udtgmt.png)](https://postimg.cc/hhcKfPyD)
- Dropout, Batch Normalization, Data Augmentation
- Kết quả accuracy trên tập train: 97.76%, accuracy trên tập validation: 94.49%, accuracy trên tập test: 94.72%

### 4. Mô hình ResNet50
[![udtgmt.png](https://i.postimg.cc/LhKqqtYK/udtgmt.png)](https://postimg.cc/8f4k9rmt)
- Kết quả accuracy trên tập train: 99.04%, kết quả accuracy trên tập test: 92.61%.
