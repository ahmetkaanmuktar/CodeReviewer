# AI Senior Code Reviewer 🕵️‍♂️💻

Bu araç, **Senior Tech Lead** gibi davranan ve kodunuzu Clean Code, Performans, Güvenlik ve Best Practices açılarından inceleyen bir CLI (Komut Satırı) uygulamasıdır.

## Kurulum 🛠️

## Kurulum ve Kullanım 🛠️

Bu projeyi kendi bilgisayarınızda çalıştırmak için adımları izleyin:

1. **Projeyi İndirin (Clone):**
   ```bash
   git clone https://github.com/ahmetkaanmuktar/CodeReviewer.git
   cd CodeReviewer
   ```

2. **Gereksinimleri Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **API Anahtarı Alın (Ücretsiz):**
   - [Google AI Studio](https://aistudio.google.com/app/apikey) adresine gidip ücretsiz bir API Key oluşturun.
   - Proje klasöründeki `.env.example` dosyasının adını `.env` yapın.
   - Anahtarınızı dosyanın içine yapıştırın:
     ```
     GEMINI_API_KEY=AIzaSy...
     ```

4. **Çalıştırın:**
   Terminali açın ve incelemek istediğiniz dosya yolunu vererek çalıştırın:
   ```bash
   python main.py dosya_adi.py
   ```

   Örnek test dosyasını denemek için:
   ```bash
   python main.py test_code.py
   ```

## Özellikler ✨
- 🧠 **Senior Tech Lead Persona**: Sadece hata bulmaz, eğitir ve vizyon katar.
- 🎨 **Rich Terminal UI**: Çıktılar renklendirilmiş ve markdown formatında okunabilir şekilde sunulur.
- ⚡ **Canlı Akış**: Analiz yapılırken sonuçlar anlık olarak ekrana düşer.
