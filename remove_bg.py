from PIL import Image
import os

def remove_white_bg(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()
    new_data = []
    
    # Tolerancia para considerar "blanco" (por la compresión JPG)
    threshold = 220
    
    for item in datas:
        # Si el píxel es casi blanco, lo hacemos transparente
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(out_path, "PNG")
    print("Logo convertido exitosamente a PNG transparente.")

if __name__ == "__main__":
    remove_white_bg("assets/images/logo.jpg", "assets/images/logo.png")
