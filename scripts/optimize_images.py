import os
import tempfile
from PIL import Image

def optimize_images(directory):
    stats = {"original_saved": 0, "webp_created": 0, "total_files": 0}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                original_size = os.path.getsize(file_path)
                stats["total_files"] += 1
                
                try:
                    with Image.open(file_path) as img:
                        # 1. Gerar versão WebP
                        webp_path = os.path.splitext(file_path)[0] + '.webp'
                        img.save(webp_path, 'WEBP', quality=80)
                        stats["webp_created"] += 1
                        
                        # 2. Tentar otimizar original em um arquivo temporário
                        tmp_path = file_path + ".tmp"
                        
                        if file.lower().endswith('.png'):
                            img.save(tmp_path, 'PNG', optimize=True)
                        else:
                            img.save(tmp_path, 'JPEG', quality=85, optimize=True)
                        
                        new_size = os.path.getsize(tmp_path)
                        
                        if new_size < original_size:
                            # Se for menor, substitui
                            os.replace(tmp_path, file_path)
                            stats["original_saved"] += 1
                            print(f"✓ {file}: {original_size/1024:.1f}KB -> {new_size/1024:.1f}KB")
                        else:
                            # Se for maior, descarta a otimização do original
                            os.remove(tmp_path)
                            print(f"- {file}: Mantido original (otimização aumentaria o tamanho)")
                            
                except Exception as e:
                    print(f"✗ Erro em {file}: {e}")

    print("-" * 30)
    print(f"Concluído! {stats['webp_created']} WebPs criados, {stats['original_saved']}/{stats['total_files']} arquivos originais reduzidos.")

if __name__ == "__main__":
    img_dir = "img"
    if os.path.exists(img_dir):
        optimize_images(img_dir)
    else:
        print(f"Diretório {img_dir} não encontrado.")
