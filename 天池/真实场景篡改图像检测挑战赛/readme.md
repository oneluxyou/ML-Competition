

使用官方提供的baseline：MVSSNet







##Part Detail
input                       (2, 3, 512, 512)
size取输入的后两位             （512， 512）

input_ = input.clone()      (2, 3, 512, 512)

feature_map, _ = self.base_forward(input_)
c1, c2, c3, c4 = feature_map
feature_map[0]:torch.Size([2, 256, 128, 128])
feature_map[1]:torch.Size([2, 512, 64, 64])
feature_map[2]:torch.Size([2, 1024, 32, 32])
feature_map[3]:torch.Size([2, 2048, 32, 32])





