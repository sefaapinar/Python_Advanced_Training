#Comment isminde bir sınıf oluşturunuz.
# Comment sınıfı username, text, likes, dislikes isminde özellikler sahip olsun.
# 5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırın.


class Comment:
    def __init__(self,username,text,likes=0,dislikes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

c1 = Comment("sefapinar","Great project.")
c2 = Comment("ahmetcansız","Bad project.",5,400)
c3 = Comment("sevvalcan","Good vibe project.",40,800)
c4 = Comment("tamerbaba","Experince")
c5 = Comment("sefapinar","Great project.",100)


comments = [c1,c2,c3,c4,c5]
for c in comments:
    print(f"{c.username}: {c.text}")
    print(f"likes: {c.likes} - dislikes {c.dislikes}")


        