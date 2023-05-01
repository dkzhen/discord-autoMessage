import asyncio
import discord
import os

os.system('pip install -U discord==1.7.3')
os.system('pip install -U discord.py==1.7.3')


# https://www.youtube.com/watch?v=YEgFvgg7ZPI
token = ''
# Message to reply with when somebody DMs the token.
replyMessage = 'Join discord.gg/ to buy limiteds!'
# Message to send in the channel.
mainMessage = 'Malam guys'
chatMsg = ['malam guys', 'semangat kawan',
           'jangan tipes sebelum JP', "Akuntansi keuangan menengah ke bawah", "Hanya untuk dapat hidup bersamamu", "Hanya untuk mencari tempat berlabuhmu", 'Kebelet jp pada ngebadut', 'Saya benar-benar percaya bahwa proyek ini akan sangat membantu untuk membuat kita tersenyum.', 'Saya berharap proyek ini akan berkembang dengan baik dan akan berada di bulan', 'Saya mulai menyukai proyek ini, saya Hanya berharap dan berdoa agar proyek ini berhasil', 'saya akan mencoba keberuntungan saya proyek anda sangat bagus', 'Saya benar-benar percaya bahwa proyek ini akan sangat membantu untuk membuat kita tersenyum. Saya berharap proyek ini akan berkembang dengan baik dan akan berada di bulan.',
           'Saya mulai menyukai proyek ini, saya. Hanya berharap dan berdoa agar proyek ini berhasil, saya akan mencoba keberuntungan saya',
           'proyek anda sangat bagus, whitepapernya juga sangat jelas, semoga proyek anda bisa sukses dan sukses kedepannya, saya juga berharap komunitasnya bisa berkembang lebih besar lagi dari sekarang',
           'Token Ini Akan Booming Dan Direkomendasikan Untuk Teman Kripto Saya, Jangan Berpikir Lebih Lanjut, Ikuti Saja',
           'Hal terindah di dunia tidak bisa disentuh, tidak bisa dilihat dengan mata, harus dirasakan hanya dengan hati-cinta, kebaikan, ketulusan.',
           'Tim ini adalah salah satu tim terbaik di dunia crypto, saya sangat senang menjadi bagian dari tim yang paling membanggakan ini.. Semoga beruntung',
           'Proyek bagus berikutnya ini adalah proyek bagus ke depan. semoga menjadi harapan baru dan memberikan kemajuan yang baik',
           'Saya berharap Anda sukses dalam kampanye yang berharga ini. Saya di sisi Anda dan saya akan mencoba menambahkan yang lain. Terima kasih.',
           'Proyek yang bagus dan tim yang kuat dalam peta jalan yang dapat diprediksi dan transparan, direncanakan dan diproyeksikan. Saya pikir dalam waktu dekat kita akan melihat pertumbuhan yang belum pernah terjadi sebelumnya dari proyek ini.',
           'Proyek yang luar biasa, proyek ini sangat bagus dan proyektor ini memiliki banyak daya tarik, semoga proyek ini menjadi lebih baik di masa depan dan cryptocurrency akan menjadi yang terbaik'
           ]
channelId = 1062167778183876648  # Channel ID to send the messages in.
delay = 25  # Delay between each message in seconds.
jarak = 10


class Main(discord.Client):
    async def on_ready(self):
        print('Logged in as %s.' % self.user)
        while True:
            for i in chatMsg:
                channel = self.get_channel(channelId)
                await channel.send(i)
                print('Sent message in #%s.' %
                      channel.name+'dengan pesan %s' % i)
                await asyncio.sleep(delay)

    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id != self.user.id:
                with open('blacklist.txt', 'r', encoding='UTF-8') as file:
                    if str(message.author.id) not in file.read():
                        await message.reply(replyMessage)
                        print('Replied to %s.' % message.author.name)
                        with open('blacklist.txt', 'a', encoding='UTF-8') as file:
                            file.write('%s\n' % message.author.id)


if __name__ == '__main__':
    Main().run(token, bot=False)
