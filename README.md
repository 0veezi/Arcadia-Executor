# Discord Ticket Bot

## Açıklama
Bu proje, Discord sunucularında kullanıcıların destek taleplerini yönetmek için bir ticket botu oluşturmayı amaçlamaktadır. Bot, kullanıcıların butonlar aracılığıyla ticket açmalarını sağlar ve yetkililerin bu ticket'ları yönetmesine olanak tanır.

## Özellikler
- Kullanıcıların buton ile ticket açabilmesi.
- Ticket'ların özel kanallarda yönetilmesi.
- Yetkililerin ticket'lara yanıt verebilmesi ve ticket'ları kapatabilmesi.
- Ticket işlemlerinin loglanması.
- Kullanıcı ve yetkili rolleri ile erişim kontrolü.

## Gereksinimler
- Python 3.8 veya üzeri
- `discord.py` kütüphanesi
- `discord_buttons_plugin` kütüphanesi

## Kurulum
1. Bu repository'yi klonlayın:
   ```bash
   git clone https://github.com/0veezi/Discord-Ticket-Bot.git
   cd Discord-Ticket-Bot
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install discord.py discord-buttons
   ```

3. `.env` dosyasını oluşturun ve gerekli bilgileri doldurun:
   ```plaintext
   DISCORD_TOKEN=your_discord_bot_token_here
   GUILD_ID=your_guild_id_here
   STAFF_ROLE_ID=your_staff_role_id_here
   TICKET_CATEGORY_ID=your_ticket_category_id_here
   ```

## Kullanım
- Botu çalıştırmak için aşağıdaki komutu kullanın:
   ```bash
   python bot.py
   ```

- Kullanıcılar, botun gönderdiği "Ticket Aç" butonuna tıklayarak yeni bir ticket oluşturabilirler.

## Katkıda Bulunanlar
- [Durmuş](https://github.com/0veezi)

## Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.
