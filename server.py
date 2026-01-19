import io
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PIL import Image
import torch
import torchvision.transforms as transforms

# HuggingFace AnimeGAN2 modelini yükle
model_name = "bryandlee/animegan2-pytorch:face_paint_512_v2"
model = torch.hub.load("bryandlee/animegan2-pytorch", "generator", pretrained="face_paint_512_v2")
model.eval()

app = FastAPI()

# Görüntü dönüşüm fonksiyonu
def transform_image(image: Image.Image) -> Image.Image:
    transform = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor()
    ])
    img = transform(image).unsqueeze(0)
    with torch.no_grad():
        out = model(img)[0]
    out = (out * 0.5 + 0.5).clamp(0, 1)  # normalize
    out_img = transforms.ToPILImage()(out.cpu())
    return out_img

@app.post("/convert")
async def convert_image(file: UploadFile = File(...)):
    # Görüntüyü oku
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    # AnimeGAN dönüşümü uygula
    anime_img = transform_image(image)

    # Yanıtı byte stream olarak döndür
    buf = io.BytesIO()
    anime_img.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")

