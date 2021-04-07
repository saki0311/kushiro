from django.shortcuts import render
from django.http import HttpResponse
from .models import LabUser

import torch

def index(request):
    return render(request,'index.html')



def predict():
    # 学習モデルの読み込み
    # モデルの定義が必要？？？
    model_path = 'xxxx.pth'
    model.load_state_dict(torch.load(model.pth, map_location=torch.device('cpu')))
    model = model.eval()

    # 推定する画像の読み込み
    PATH = "xxxxxx.jpg"
    image = Image.open(PATH)
    image = ImageOps.invert(image)
    image = image.convert('L').resize((28,28))
    # データの前処理の定義(モデル生成の際と同じ平均値と標準偏差で正規化する)
    transform = transforms.Compose([
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.1307,), (0.3081,))
                                    ])

    # 元のモデルに合わせて次元を追加
    image = transform(image).unsqueeze(0)


    # 予測
    output = model(image.to(device))
    _, prediction = torch.max(output, 1)

    # 予測結果を返す
    print("{} -> result = ".format(PATH) + str(prediction[0].item())) #よくわからん


