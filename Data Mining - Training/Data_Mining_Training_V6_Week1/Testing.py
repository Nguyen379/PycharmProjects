import string
van_ban = '''
OLYMPIA: NHÂN TÀI CHO NƯỚC ÚC, CÂU CHUYỆN Ở LẠI HAY VỀ NƯỚC CỐNG HIẾN. Sau mỗi trận chung kết Đường lên đỉnh Olympia, 
câu nói được sử dụng nhiều nhất không phải là những lời chúc mừng dành cho đường kim vô địch, mà là câu nói: “Chúc 
mừng nước Úc có thêm một nhân tài”. Hoặc là: “Ở Việt Nam sẽ bị con ông cháu cha vùi dập”. Nếu nhà vô địch của Đường 
lên đỉnh Olympia là một thiên tài, vậy thì Á quân, hai người đồng hạng Ba, có phải là nhân tài hay không? Rồi những 
nhà vô địch các cuộc thi Tuần, thi Quý, thi Tháng, có phải là nhân tài hay không? Mỗi năm, có khoảng gần 150 nhà 
“leo núi”, mà bất cứ một nhà leo núi nào cũng đều tài năng, giỏi giang tại ngôi trường của họ, và đa phần họ sẽ ở lại 
Việt Nam để học tập, làm việc và cống hiến. Chỉ một người ra đi thôi, mà họ đã bị quan cực độ, chửi bới Việt Nam 
rằng “để mất chất xám”, vậy hóa ra, cả Việt Nam chỉ có một nhân tài thôi à?
'''
print(''.join([tu for tu in list(van_ban) if not tu in string.punctuation]).split())
