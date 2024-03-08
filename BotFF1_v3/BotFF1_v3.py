import discord
from discord.ext import commands
import requests
import random
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def halo(ctx):
    await ctx.send(f'''
# Hai! Saya {bot.user}!
## Hal yang bisa saya lakukan:
- **Menulis kata/kalimat dengan suku kata berulang. Perintah:**
 - ```!he 10```*
 - ```!wk 10```*
 - ```!hi 10```*
 - ```!ha 10```*
 - ```!hiks 10```*
 - ```!ho 10```*
 - ```!hu 10```*
 - ```!uhuk 10```*
 - ```!prok 10```*
 - *Jumlah perulangan. Ganti dengan jumlah perulangan yang Anda butuhkan atau mengosongkannya
- **Menghitung operasi 2 angka. Perintah:**
 - ```!penjumlahan 6 2```**
 - ```!pengurangan 6 2```**
 - ```!perkalian 6 2```**
 - ```!pembagian 6 2```**
 - ```!pembagian_bilangan_bulat 6 2```**
 - ```!perpangkatan 6 2```**
 - **Angka yang akan dioperasikan. Ganti dengan angka yang Anda butuhkan
 - **Menampilkan meme. Perintah:**
 - ```!meme_pemrograman_1```
 - ```!meme_pemrograman_2```
 - ```!meme_pemrograman_3```
 - ```!meme_pemrograman_acak```
- **Melempar koin. Perintah:**
 - ```!lempar_koin```
- **Menampilkan emoji. Perintah:**
 - ```!emoji_acak_klasik```
 - ```!emoji_acak_bahagia```
 - ```!emoji_acak_salam```
 - ```!emoji_acak_bertindak_lucu```
 - ```!emoji_acak_sedih```
 - ```!emoji_acak_marah```
 - ```!emoji_acak_terkejut_terdiam```
- **Membuat sandi kuat. Perintah:**
 - ```!buat_sandi 10```***
 - ***Jumlah karakter sandi. Ganti dengan jumlah karakter yang Anda butuhkan atau mengosongkannya
- **Menampilkan kiat-kiat tentang lingkungan. Perintah:**
 - ```!menerapkan_gaya_hidup_ramah_lingkungan```
 - ```!cara_mengurangi_limbah```
- **Menampilkan fakta tentang ketergantungan teknologi. Perintah:**
 - ```!fakta_acak_tentang_ketergantungan_teknologi```
- **Menampilkan gambar & gif tentang bebek. Perintah:**
 - ```!bebek```
''')

@bot.command()
async def he(ctx, count_he = 3):
    await ctx.send("```"+"he" * count_he+"```")

@bot.command()
async def wk(ctx, count_wk = 3):
    await ctx.send("```"+"wk" * count_wk+"```")

@bot.command()
async def hi(ctx, count_hi = 3):
    await ctx.send("```"+"hi" * count_hi+"```")

@bot.command()
async def ha(ctx, count_ha = 3):
    await ctx.send("```"+"ha" * count_ha+"```")

@bot.command()
async def hiks(ctx, count_hiks = 3):
    await ctx.send("```"+"hiks " * count_hiks+"```")

@bot.command()
async def ho(ctx, count_ho = 3):
    await ctx.send("```"+"ho" * count_ho+"```")

@bot.command()
async def hu(ctx, count_hu = 3):
    await ctx.send("```"+"hu" * count_hu+"```")

@bot.command()    
async def uhuk(ctx, count_uhuk = 3):
    await ctx.send("```"+"uhuk " * count_uhuk+"```")

@bot.command()
async def prok(ctx, count_prok = 3):
    await ctx.send("```"+"prok " * count_prok+"```")

@bot.command()
async def penjumlahan(ctx, x:int, y:int):
    await ctx.send("Hasilnya: ```"+str(x+y)+"```")

@bot.command()
async def pengurangan(ctx, x:int, y:int):
    await ctx.send("Hasilnya: ```"+str(x-y)+"```")

@bot.command()
async def perkalian(ctx, x:int, y:int):
    await ctx.send("Hasilnya: ```"+str(x*y)+"```")

@bot.command()
async def pembagian(ctx, x:int, y:int):
    await ctx.send("Hasilnya: ```"+str(x/y)+"```")

@bot.command()
async def pembagian_bilangan_bulat(ctx, x:int, y:int):
    await ctx.send("Hasilnya: ```"+str(x//y)+"```")

@bot.command()
async def perpangkatan(ctx, x:int, y:int):
    await ctx.send("Hasilnya: ```"+str(x**y)+"```")

@bot.command()
async def meme_pemrograman_1(ctx):
    with open('meme_p_1.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def meme_pemrograman_2(ctx):
    with open('meme_p_2.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def meme_pemrograman_3(ctx):
    with open('meme_p_3.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def meme_pemrograman_acak(ctx):
    mm = random.randint(0,2)
    if mm == 0:
        with open('meme_p_1.png', 'rb') as f:
            meme1 = discord.File(f)
            await ctx.send(file=meme1)
    elif mm == 1:
        with open('meme_p_2.png', 'rb') as f:
            meme2 = discord.File(f)
            await ctx.send(file=meme2)
    elif mm == 2:
        with open('meme_p_3.png', 'rb') as f:
            meme3 = discord.File(f)
            await ctx.send(file=meme3)
    

@bot.command()
async def lempar_koin(ctx):
    coin = ['# Kepala','# Ekor']
    await ctx.send(random.choice(coin))

@bot.command()
async def emoji_acak_klasik(ctx):
    emoji_klasik = [';)','^_~',';-)',':)','^_^',':-)',':D','^0^',':-D',':P',':-P',';P',':(',':-(','U_U',':[','>:(','>"<','):',':-O','O.O',':-()','~_~','^o^',':-S','<3','^3^',':-x',':/','X_X','=/',';(','T_T',';[','+_+','O_O',':O','¬_¬',';_;','=.=',';]','^_+',';O)',':-]','^.^','=)',':O)',':-3','=D',':|','-.-','>_<',':O(','*_*','=[','8-)','^^;',':-*','B-)','=_=','-0-',':S','$_$',':-$','>.<','-_-','> <',':]','^^','=]',';D','^_-','=P',":'(",'Y.Y','=(']
    await ctx.send("```"+random.choice(emoji_klasik)+"```")

@bot.command()
async def emoji_acak_bahagia(ctx):
    emoji_bahagia = ['ヾ(≧▽≦*)o','φ(*￣0￣)','q(≧▽≦q)','ψ(｀∇´)ψ','（￣︶￣）↗','*^____^*','(～￣▽￣)～','( •̀ ω •́ )✧','[]~(￣▽￣)~*','φ(゜▽゜*)♪','o(*^＠^*)o','O(∩_∩)O','(✿◡‿◡)','`(*>﹏<*)′','(*^▽^*)','（*＾-＾*）','(*^_^*)','(❁´◡`❁)','(≧∇≦)ﾉ','(´▽`ʃ♡ƪ)','(●ˇ∀ˇ●)','○( ＾皿＾)っ Hehehe…','(￣y▽￣)╭ Ohohoho.....','\^o^/','(‾◡◝)','╰(*°▽°*)╯','(〃￣︶￣)人(￣︶￣〃)','o(*^▽^*)┛','o(*￣▽￣*)ブ','(^_-)db(-_^)','o(*￣▽￣*)ブ','♪(^∇^*)','(≧∀≦)ゞ','o(*￣︶￣*)o','--<-<-<@','(oﾟvﾟ)ノ','o(*≧▽≦)ツ┏━┓','(/≧▽≦)/','( $ _ $ )','(☆▽☆)','ヾ(＠⌒ー⌒＠)ノ','ㄟ(≧◇≦)ㄏ','o((>ω< ))o','( *︾▽︾)','ヾ(≧ ▽ ≦)ゝ','☆*: .｡. o(≧▽≦)o .｡.:*☆','(((o(*ﾟ▽ﾟ*)o)))','♪(´▽｀)','＼(((￣(￣(￣▽￣)￣)￣)))／','( *^-^)ρ(^0^* )','~~~///(^v^)\\\~~~','(^///^)','(p≧w≦q)','o(*￣▽￣*)o','( •̀ ω •́ )y','(o゜▽゜)o☆','ƪ(˘⌣˘)ʃ']
    await ctx.send("```"+random.choice(emoji_bahagia)+"```")

@bot.command()
async def emoji_acak_salam(ctx):
    emoji_salam = ['ヾ(•ω•`)o','\(￣︶￣*\))','(* ￣3)(ε￣ *)','－O－','(*￣3￣)╭','( ´･･)ﾉ(._.`)','(｡･∀･)ﾉﾞ','o(*￣▽￣*)ブ','(_　_)。゜zｚＺ','(ToT)/~~~','(∪.∪ )...zzz','!(*￣(￣　*)','(￣o￣) . z Z','(づ￣ 3￣)づ','（＾∀＾●）ﾉｼ','（づ￣3￣）づ╭❤～','\(@^0^@)/','ヾ(^▽^*)))','(～﹃～)~zZ','☆⌒(*＾-゜)v','(￣o￣) . z Z','(*￣;(￣ *)','||ヽ(*￣▽￣*)ノミ|Ю','☆⌒(*＾-゜)v','(＾Ｕ＾)ノ~ＹＯ','o(*°▽°*)o','ヾ(￣▽￣) Bye~Bye~','( ﾟдﾟ)つ Bye','(๑•̀ㅂ•́)و✧','(o゜▽゜)o☆','✪ ω ✪','d=====(￣▽￣*)b','＜（＾－＾）＞','o(*￣▽￣*)o','o(￣▽￣)ｄ','(╹ڡ╹ )','(u‿ฺu✿ฺ)','♪(´▽｀)','(╯▽╰ )','ヽ(✿ﾟ▽ﾟ)ノ','( •̀ .̫ •́ )✧','(^^ゞ','(＠＾０＾)','（。＾▽＾）','Ψ(￣∀￣)Ψ','*★,°*:.☆(￣▽￣)/$:*.°★* 。','(。・∀・)ノ','~\(≧▽≦)/~','b(￣▽￣)d','o(^▽^)o','(☞ﾟヮﾟ)☞','☜(ﾟヮﾟ☜)','(¬‿¬)','(•_•)','( •_•)>⌐■-■','(⌐■_■)']
    await ctx.send("```"+random.choice(emoji_salam)+"```")

@bot.command()
async def emoji_acak_bertindak_lucu(ctx):
    emoji_bertindak_lucu = ['(￣y▽,￣)╭ ','(o|o) ','(^人^)','§(*￣▽￣*)§','ψ(._. )>','(/▽＼)','(o′┏▽┓｀o) ','(*≧︶≦))(￣▽￣* )ゞ','(　o=^•ェ•)o　┏━┓','◑﹏◐','(○｀ 3′○)','(ಥ _ ಥ)','(⓿_⓿)','(❤´艸｀❤)','(ง •_•)ง','（〃｀ 3′〃）',"(●'◡'●)",'o(〃＾▽＾〃)o','(。・ω・。)','(✿◠‿◠)','ˋ( ° ▽、° ) ','(*/ω＼*)','=￣ω￣=','ο(=•ω＜=)ρ⌒☆','(✿◕‿◕✿)','╰(￣ω￣ｏ)','~(￣▽￣)~*','(～o￣3￣)～','(っ´Ι`)っ','ԅ(¯﹃¯ԅ)','(￣﹃￣)','༼ つ ◕_◕ ༽つ','o(*////▽////*)q','(^///^)','(/ω＼*)……… (/ω•＼*)','(o゜▽゜)o☆','( ‵▽′)ψ','( ﹁ ﹁ ) ~→','(❤ ω ❤)','(★ ω ★)','ヽ(￣ω￣(￣ω￣〃)ゝ','*(੭*ˊᵕˋ)੭*ଘ','┏ (゜ω゜)=☞','U•ェ•*U','（￣。。￣）','(°°)～','m( =∩王∩= )m','o(=•ェ•=)m','(‧‧)nnn','\(0^◇^0)/','~o( =∩ω∩= )m','--\(˙<>˙)/--','( ఠൠఠ )ﾉ','≡[。。]≡','(:≡','．<{=．．．．','ฅʕ•̫͡•ʔฅ','( ⓛ ω ⓛ *)','ᓚᘏᗢ','( ¯(∞)¯ )','(￣(工)￣)','<。)#)))≦','(:◎)≡','^(*￣(oo)￣)^','( ͡• ͜ʖ ͡• )','¯\_(ツ)_/¯']
    await ctx.send("```"+random.choice(emoji_bertindak_lucu)+"```")

@bot.command()
async def emoji_acak_sedih(ctx):
    emoji_sedih = ['（；´д｀）ゞ','＞﹏＜','(っ °Д °;)っ','(￣ ‘i ￣;)','( *^-^)ρ(*╯^╰)','＞︿＜','o(￣┰￣*)ゞ','(ノへ￣、)','<(＿　＿)>','(#｀-_ゝ-)','（＞人＜；）','{{{(>_<)}}}','≡(▔﹏▔)≡','(#_<-)','⊙﹏⊙∥','ヽ(*。>Д<)o゜','/(ㄒoㄒ)/~~','(;´༎ຶД༎ຶ`)','::>_<::','╯︿╰','இ௰இ','(┬┬﹏┬┬)','(´。＿。｀)','(；′⌒`)','≧ ﹏ ≦','〒▽〒','━((*′д｀)爻(′д｀*))━!!!!','(T_T)','(≧﹏ ≦)','(′д｀ )…彡…彡','<( _ _ )>','o(TヘTo)','~~>_<~~','┗( T﹏T )┛','(。﹏。*)','X﹏X','ಥ_ಥ']
    await ctx.send("```"+random.choice(emoji_sedih)+"```")

@bot.command()
async def emoji_acak_marah(ctx):
    emoji_marah = ['o((>ω< ))o','╰（‵□′）╯','(～￣(OO)￣)ブ','o(≧口≦)o','(╬▔皿▔)╯','(⊙x⊙;)','￣へ￣','（︶^︶）','(* ￣︿￣)','ヽ（≧□≦）ノ','╰(艹皿艹 )','___*( ￣皿￣)/#____','(￣ε(#￣)☆╰╮o(￣皿￣///)','<( ￣^￣)(θ(θ☆( >_<','(￣ε(#￣)','╰（‵□′）╯','(ﾟДﾟ*)ﾉ','○|￣|_ =3','┗|｀O′|┛','(′д｀σ)σ','(ノ｀Д)ノ','(￢︿̫̿￢☆)','～(　TロT)σ','(〃＞目＜)','(///￣皿￣)○～','<( ‵□′)>───Ｃε(┬﹏┬)3','<( ‵□′)───C＜─___-)||','ε=( o｀ω′)ノ','(ｏ ‵-′)ノ”(ノ﹏<。)','ヾ(≧へ≦)〃','(╯▔皿▔)╯','(σ｀д′)σ','ヽ(゜▽゜　)－C<(/;◇;)/~','(╯‵□′)╯︵┻━┻','┳━┳ ノ( ゜-゜ノ)','(╯°□°）╯︵ ┻━┻','(ヘ･_･)ヘ┳━┳','o(一︿一+)o','(￣﹏￣；)','ಠ_ಠ','ಠಿ_ಠ','(¬_¬ )','(¬_¬")']
    await ctx.send("```"+random.choice(emoji_marah)+"```")

@bot.command()
async def emoji_acak_terkejut_terdiam(ctx):
    emoji_terkejut_terdiam = ['w(ﾟДﾟ)w','┗|｀O′|┛','（⊙ｏ⊙）','(＃°Д°)','（*゜ー゜*）','(。_。)','...(*￣０￣)ノ','o((⊙﹏⊙))o.','(⊙ˍ⊙)','(⊙_⊙)？','(⊙_⊙;)','(⊙o⊙)','⊙.☉','¯\(°_o)/¯','(´･ω･`)?','(￣┰￣*)','o(><；)oo','Σ(っ °Д °;)っ','∑( 口 ||','┌(。Д。)┐','(°ー°〃)','ε=ε=ε=(~￣▽￣)~','(￣m￣）','(ノω<。)ノ))☆.。','(ﾉ*･ω･)ﾉ','(#`O′)','щ(ʘ╻ʘ)щ','（o´・ェ・｀o）','(*Φ皿Φ*)','(・∀・(・∀・(・∀・*)','(○´･д･)ﾉ','┬┴┬┴┤(･_├┬┴┬┴','(o_ _)ﾉ','(＠_＠;)','ㄟ( ▔, ▔ )ㄏ','(￣_,￣ )','(+_+)?','(。>︿<)_θ','<(￣ c￣)y▂ξ','(๐॔˃̶ᗜ˂̶๐॓)','o_o','━┳━　━┳━','━━(￣ー￣*|||━━',"……]((o_ _)'彡☆",'(。﹏。)','(⊙﹏⊙)','...( ＿ ＿)ノ｜',',,ԾㅂԾ,,','m( _ _ )m','(lll￢ω￢)','╮(╯-╰)╭','(￣▽￣)"','(￣_￣|||)','_〆(´Д｀ )','(x_x)','( ╯□╰ )','⊙﹏⊙∥','┌( ´_ゝ` )┐','－_-b','(ˉ﹃ˉ)','╮（╯＿╰）╭','(￣_,￣ )','○|￣|_','(ˉ▽￣～)','(´ｰ∀ｰ`)','(。・・)ノ','_(:з)∠)_','┑(￣Д ￣)┍','ε=ε=ε=┏(゜ロ゜;)┛','(*￣rǒ￣)','つ﹏⊂','(￣、￣)','╮(╯▽╰)╭','(☆-ｖ-)','(ˉ▽ˉ；)...','(◎﹏◎)','(((φ(◎ロ◎;)φ)))','<@_@>','→_→','←_←']
    await ctx.send("```"+random.choice(emoji_terkejut_terdiam)+"```")

@bot.command()
async def buat_sandi(ctx, pass_length = 15):
    elements = "1234567890-qwertyuiopasdfghjklzxcvbnm,./!@#$%&*_+QWERTYUIOPASDFGHJKLZXCVBNM?"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    await ctx.send("||```"+password+"```||")

@bot.command()
async def menerapkan_gaya_hidup_ramah_lingkungan(ctx):
    await ctx.send('''
## Menerapkan Gaya Hidup Ramah Lingkungan:
- Kurangi Penggunaan Plastik Sekali Pakai
- Hemat Energi di Rumah
- Gunakan Transportasi Berkelanjutan
- Daur Ulang
- Menghemat Air
- Minimalkan Pemakaian Bahan Kimia yang Berbahaya
- Mengurangi Konsumsi Daging
- Budidaya Tanaman Sendiri
- Menggunakan Produk Ramah Lingkungan
- Mengurangi Pemborosan Makanan
- Mendukung Komunitas Lokal
- Kurangi Penggunaan Air Botol
- Gunakan Produk Keanekaragaman Hayati yang Bertanggung Jawab
- Menggunakan Kertas Secara Bijaksana
- Kurangi Penggunaan Bahan Bakar Fosil
- Mendukung Pengembangan Ramah Lingkungan
- Mengurangi Konsumsi Internet
Pelajari selengkapnya di https://sohib.indonesiabaik.id/article/langkah-gaya-hidup-ramah-lingkungan-ADgsj
''')
    
@bot.command()
async def cara_mengurangi_limbah(ctx):
    await ctx.send('''
## Cara Mengurangi Limbah:
- Tidak Menggunakan Sedotan Plastik
- Membawa Tas Belanja Sendiri
- Mempunyai dan Membawa Botol Minum Sendiri
- Membiasakan Diri Untuk Memasak Sendiri di Rumah
- Membeli Barang dalam Kemasan yang Lebih besar Untuk Waktu yang Lama
- Membatasi Penggunaan Microbeads
- Memilih Es Krim Cone dibandingkan Es Krim Cup
- Hindari Mengonsumsi Permen Karet
- Membatasi Penggunaan Plastik dalam Membungkus Paket
- Menggunakan Bahan Bekas yang Bisa Dipakai Lagi
- Membuat Tas Daur Ulang dari Pembungkus Plastik
- Memanfaatkan Botol Plastik Sebagai Pot
- Mengkreasikan Botol Plastik Besar Menjadi Celengan
- Botol Plastik dirubah Menjadi Tempat Pakan Burung
- Merubah Botol Plastik Menjadi Tempat Alat Tulis
Pelajari selengkapnya di https://www.rumah.com/panduan-properti/15-cara-mengurangi-sampah-plastik-rumahan-dan-contoh-daur-ulangnya-27696
''')

@bot.command()
async def fakta_acak_tentang_ketergantungan_teknologi(ctx):
    facts_list = [
    "Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka.",
    "Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
    "Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan.",
    "Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja.",
    "Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati.",
    "Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.",
    "Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita.",
    "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini."
    ]
    await ctx.send(random.choice(facts_list))

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def bebek(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def pendeteksi(path_image):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(path_image).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)

    return class_name[2:]

@bot.command()
async def klasifikasi(ctx):
    data = ctx.message.attachments

    #kode untuk AI
    response = requests.get(list(data)[-1])
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    result = pendeteksi("image.jpg")
    
    await ctx.send(result)

bot.run("TOKEN RAHASIA ADA DI SINI")
