import discord
from random import randint, choice
from discord.ext import commands
from discord.utils import get
import datetime, pyowm 
import youtube_dl
import random
import codecs

import os
from time import sleep
import requests
from PIL import Image, ImageFont, ImageDraw
import io

client = commands.Bot( command_prefix = '$' )
client.remove_command( 'help' )


#Words

hello_words = [ 'hello', 'привет', 'првиетствую' ]
answer_words = [ 'узнать информацию', 'информация', 'инфа' ]
goodbye_words = [ 'пока', 'бывай', 'до связи' ]
bad_words = ['пидр', 'залупа', 'долбаёб', 'гандон', 'уёбок', 'еблан', 'дебил', 'пидор', 'урод', 'выблядок']
rules_word = ['правила']
server_words = ['созвать сервер', 'созвать всех', 'позвать всех', 'все']
anecdot_words = ['анекдот', 'анекдоты']
goodhight_words = ['спокойной ночи','всем спокойной ночи']
goodmorning_words = ['доброе утро', 'всем доброе утро', 'утро доброе' 'утречко']
oblivion_words = ['преисполнение']


list = [ ('''Идет сталкер по дороге видет впереди камень, а на нем написано:

НАЛЕВО - аномалии.

НАПРВО - мутанты.

ПРЯМО - кабаки и девки.

Ну сталкер постоял подумал да и пошёл себе налево.

Идёт и думает:

- Если живым вернусь надо будет спросить у мужиков что за напасть такая новая кабаки и девки!'''),


('''Заблудился сталкер, идет кричит:

- ЛЮЮЮДИИИИ!!!! ААУУУ!!! ГДЕ ВЫЫЫЫ??!! ЭЙ КТО НИБУУУУУДЬ!!!! ААУУУУУ!!! ...

Вдруг сзади его стучат по плечу. Он оборачивается, а там здоровый такой кровосос, недовольный.

Кровосос: " Ты чего орешь?!"

Сталкер: " Да вот.... того.... заблудился я.... думаю может услышит кто......."

Кровосос: " Ну я услышал, легче стало?'''),


('''Сталкер с мобилой идет по зоне, отстреливая кровососов. Звонок ....

- Алло, это БАНЯ?

- Нет, это Д-Е-Т-А-Л-Я !!!'''),


('''Ученый-сталкер с Янтаря исследует зону, кидает болты и записывает разные виды аномалий. Весь день ходил всю тетрадь исписал: уже глаза на лоб лезут. Ночью возвращается на базу, смотрит куст какой-то разворошенный один, остальные рядом нормальные растут - кидает болт. Оттуда кровосос с просони:

Кровосос (непонимая происходящего): - Ой эююй больэюйно!

Ученый-сталкер (многозначительно): - Так, новый вид аномалии под номером N255 - "Говорящая!"'''),

 
('''Приходит Сталкер к костоправу и говорит:

- Доктор, мне постоянно снится один и тот же сон: как меня в саркофаге монстры рагрывают. Что делать?

- А это вас Контролер предупреждает! В следущий раз поставьте ему бутылочку, а то еще, не ровен час, сон в явь превратится...

- Спасибо Доктор..

- Да не что, это тебе за Доктора спасибо-, говорит Контроллер - мелочи, а приятно..'''),


('''Сидят два Сталкера, один другому говорит:

- Че это чушь всякую про Зону порят, что мол опасно тут, радиация!! Вот Я уже 5 лет по Зоне шарюсь и НИЧЕГО!!

-...Хотя нет, чешуя че-то в последнее время чесаться стала сильнее...."'''),



('''Встречаются два Сталкера, один другому говорит:

-Ты Васю помнишь, ну того, что в летное поступить хотел...

-Ну и...

-Так он на днях в трамплин попал!! Да, сбылась у человека мечта - ПОЛЕТЕЛ...


Идет военный контрактник по зоне, отбился и орет:"Л-л-л-ю-ю-ю-д-д-д-и-и-и-и....Кто-нибудь есть?".

Ав кустах Сталкер сидит и думает:" А, как потерялся так ЛЮДИ, а как по тыкве бить прикладом так СОБАКИ..."'''),


('''Сталкеру Новый русский говорит:"ты мне Золотую рыбку достань, а то все люди как люди, я один такой ЛОХ...".

Сталкер в недоумении:" Так он...это....радиоактивный.."

-Радиоактивный, радиопассивный НЕ в трусы же я его положу! А на желтявую цепь, чтоб как у людей было...'''),


('''Тренерует Контролер слепого пса сальто назад делать, проходит мимо зомби и смотрит так недоверчиво и говорит:" Да брось Ты это, харе страдать.."

А контролер отвечает:" Вот ты Сталкер, тоже поначалу плохо слушался..."'''),



('''На базе Свободы мужика шифером убило. Все собрались, сочувствуют, охают...и пригляделись, а это не мужик, а зомби..

Думаете они блокпосты пошли укреплять, патрули...Нихрена подобного!! Токо раскудахтались опять мол, развелось монстров, даже шиферу упасть некуда'''),



('''Не разъехались в Зоне бандиты с наемниками, ну и подоставали пушки, палить стали. А контролер, что у перекрестка сидел говорит про себя:" Вот удачно место выбрал, давно хотел посмотреть нормальные пацанские разборки..."'''),


('''Старый и молодой Долговцы идут, вдруг старый тормозит молодого и говорит на ухо:" Ложись и ползи до того дерева." Ну молодой дополз, встает и смотрит на старого, че типа дальше делать, а старый как заорет:" Говорил, что брешут: нет тут никакой аномалии!'''),



('''Захватил контроллер военного, учённого и сталкера. Привёл их на крышу заброшенного завода, и говорит им:

- Внизу натянут тент, кто прыгнет и на тент попадёт того я отпущу.

Военный, не долго думая, прыгнул - разбился. Учённый быстро посчитал, прикинул, всё учёл, прыгнул и попал на тент, в общем, спасся.

Сталкер думает: "Ну учённый всё сосчитал, я сейчас так-же сделаю". Разбегается, прыгает и с воплем: "Б@*, опять в аномалию попал!" - улетает в небо...'''),



('''Захватили Сталкеры в плен Зомбака.

-Зомбак, сколько монстряков охраняет саркофаг?

-С Контроллером - 25 монстряков!

-А без Контроллера?

-Нисколько...'''),


('''Общаются два карлика:

Первый- «Сталкеры совсем оборзели, устроили мне подлянку... Повесили над выходом ведро с водой, я ночью вышел, ну меня всего и окотило.»

Второй - «Ну ты уж вообще к ним придираешься, вот уж мелочь какая ведро с водой»

- «Мелочь говоришь! Так они туда еще и запах собачьей самки, во время течки подмешали… Я двое суток потом, от слепых псов по всей зоне бегал»'''),



('''Идут два сталкера-еврея:

- Мойша, ты знаешь, а Сема таки педараст!

- Шо, водку занял и не отдает?

- Нет, в хорошем смысле...'''),



('''Идёт по Зоне зомби. Смотрит лежит артефакт - цоп его, и идёт дальше. Вдруг догоняет его сталкер, помятый весь, глаза красные, щёки впалые - вобщем жалкое зрелище. Сталкер говорит:

- Зомби, будь другом отдай артефакт. Я за ним десять дней шёл, патроны кончились, жратва тоже. Отдай, а?.

- Фиг с два! Я нашёл - мой артефакт.

Но сталкер не отстаёт - отдай да отдай. Зомби подумал с немного и говорит:

- Хорошо. Давай кто кого сильнее по яйцам пнёт, того и артефакт.

Подумал сталкер, делать нечего согласился.

- Я первый! - говорит зомби. Разбегается и ка-а-ак вдарит сталкеру, у того всё чуть через рот не выпрыгнуло.

Очухался сталкер и говорит:

- Ну что, хорошо вошло, теперь моя очередь...

- Да на хрена мне твой артефакт. - сказал зомби, протягивая артефакт.'''),


('''Вышли три сильно пьяных Сталкера из здания заброшенного завода.

И вдруг их неожиданно начало рвать...

- Много выпил... - подумал первый Сталкер, глядя на свои заблёванные ботинки...

- Аномалия близко... - подумал второй, глядя на разлетающиеся куски третьего...'''),



('''Ползут три пьяных сталкера по рельсам из Зоны. Один говорит:

- Чёто лестница неудобная...

- И перила широкие...

- Да хрен с ним: вон лифт едет...'''),



('''Идет Сталкер по Зоне. Видит Монстряка сидит плачет, гоькими слезами обливается...

- Ты че плачешь, Монстряка? - спрашивает.

- Все меня обижают, другие Монстряки обижают, Сталкеры обижают...

- А хочешь я тебе НАКУ дам?

- Хочу - оживилась Монстряка.

Сталкер, снимает автомат и прикладом: - НАКА! НАКА! МОНСТРЯКА! ПОЛУЧИ! НАКА!!!'''),



('''Поймали Наёмники Сталкера, окунают его в воду и спрашивают:

- Деньги, бабло, артефакты есть?

Сталкер:

- Нет.

И опять окунают в воду и спрашивают:

- Деньги, бабло, артефакты есть?

Сталкер:

- Да нету, нету!

А они опять окунают :

- Деньги, бабло, артефакты есть?

Ну сталкер не выдержал:

- Блин, вы либо дольше держите, либо глубже опускайте ! Вода мутная - нихрена не видно!''') ]











#Bot status, connecting
@client.event

async def on_ready():
	print('Bot online!')

	await client.change_presence( status = discord.Status.online, activity = discord.Game( '$help' ) )


@client.event
async def on_command_error( ctx, error ):
	pass

print('Bot activated!')



#Clear message

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount : int ):
	await ctx.channel.purge( limit = 1 )
	await ctx.channel.purge( limit = amount )





#Kick

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1 )

	await member.kick( reason = reason )
	await ctx.send( f'Пользователь { member.mention }' + ' кикнут, по причине за нарушение правил!' )




#Ban

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
	emb = discord.Embed( title = 'BAN', colour = discord.Color.red() )
	await ctx.channel.purge( limit = 1 )

	await member.ban( reason = reason )

	emb.set_author( name = member.name, icon_url = member.avatar_url )
	emb.add_field( name = 'Забанен', value = 'Пользователь : {}'.format( member.mention ) )
	emb.set_footer( text = 'Был забанен администратором - {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )

	await ctx.send( embed = emb )



#Unban

@client.command( pass_context = True )

async def unban( ctx, *, member ):
	await ctx.channel.purge( limit = 1 )

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban( user )
		await ctx.send( f'Unbanned user { user.mention }' )

		return




#Filtered and message
@client.event

async def on_message( message ):
	await client.process_commands( message )

	msg = message.content.lower()

	if msg in bad_words:
		await message.delete()
		await message.author.send( f'{ message.author.mention }! Ещё раз будешь матюкаться, забаню, еблан ДИЗЕЛЬНЫЙ!' )
		sleep(3)
		await message.author.send( f'Иди делай уроки, двоечник ты!' )
		sleep(3)
		await message.author.send( f'Тебя завта в дурку забирают, так что готовься))' )
	
		print('Function: Filtered chats --- acrivated!')
		sleep(1)

	#Message reply

	if msg in anecdot_words:
		await message.channel.send(random.choice(list))

	if msg in hello_words:
		await message.channel.send( 'Привет! Рады видеть тебя на нашем сервере!' )

	if msg in answer_words:
		await message.channel.send( 'Напиши в чат команду "!help"' )

	if msg in goodbye_words:
		await message.channel.send( 'Пока! Удачи тебе!' )

	if msg in server_words:
		await message.channel.send( '@everyone' )

	if msg in goodhight_words:
		await message.channel.send( '@everyone' )
		sleep(2)
		await message.channel.send( ' НУКА НАХУЙ ВСЕ ПО ШКОНКАМ ' )

	if msg in goodmorning_words:
		await message.channel.send( '@everyone' )
		sleep(2)
		await message.channel.send( 'ПРОСЫПАЕМСЯ НАХУЙ!!!' )

	if msg in rules_word:
		await message.channel.send(''' НЕЗНАНИЕ ПРАВИЛ НЕ ОСВОБОЖДАЕТ ОТ ОТВЕТСТВЕННОСТИ!
1) Нецензурная лексика(маты) - разрешены.

2) Оскорбление и оскорбительное поведение в сторону участников беседы с целью унижения их чести и достоинства личности - запрещены
►Наказание: предупреждение◄

2.1) Админ обязан спросить того участника беседы, которого оскорбили хочет ли он простить того, кто его оскорбил, если жертва прощает обидчика, то наказание не выдаётся.

3) Спам и флуд - запрещены.
►Наказание: кик.◄

4) Срач разрешён, но в рамках разумного

5) Реклама-Пиар запрещены(беседы,группы, взаимные лайки, накрутка друзей, попросить проголосовать)
►Наказание: кик◄

6) Разрешены ссылки на приглашение в игру, discord и т.д.

7) За неактив в течении недели вы будете ИСКЛЮЧЕНЫ.

8) Приглашать людей могут только Админы(Если хотите добавить кого-то, напишите администрации).

9) Любые фото или видеоматериалы содержащие шок-контент или 18+ можно отправлять с 21:00 до 03:00 (МСК)
►Наказание: предупреждение или Кик (на усмотрение администрации)◄

10) 16+ контент(легкая эротика) - разрешены.

11) Выходить и заходить в беседу - запрещено. (Не распространяется на Администрацию)
►Наказание: Кик или предупреждение, На усмотрение администрации.◄

11.1) Если хотите выйти из беседы, пишите администратору, он вас исключит. Тем самым, при вашем желании, вы сможете вернуться обратно, всего лишь попросив у администратора.

12) Оскорбление или высмеивание администрации - запрещены. (Относится ко всему админ-составу проекта)
►Наказание: Предупреждение или Кик (по решению администрации)◄

13) Вымогательство или попрошайничество - запрещены.
►Наказание: предупреждение◄

14) Осуждение, высмеивание и шутки над религией или властью - запрещены.
►Наказание: кик ◄

15) Правила распространяются на админов на тех же условиях,что и на участников (Кроме заранее предписанных исключений) ''')



	if msg in oblivion_words:
		await message.channel.send('''Я в своем познании настолько преисполнился, что я как будто бы уже сто триллионов миллиардов лет проживаю на триллионах и триллионах таких же планет, как эта Земля, мне этот мир абсолютно понятен, 
			и я здесь ищу только одного - покоя, умиротворения и вот этой гармонии, от слияния с бесконечно вечным, от созерцания великого фрактального подобия и от вот этого замечательного всеединства существа, бесконечно вечного, 
			куда ни посмотри, хоть вглубь - бесконечно малое, хоть ввысь - бесконечное большое, понимаешь? А ты мне опять со своим вот этим, иди суетись дальше, это твоё распределение, 
			это твой путь и твой горизонт познания и ощущения твоей природы, он несоизмеримо мелок по сравнению с моим, понимаешь? Я как будто бы уже давно глубокий старец, бессмертный, 
			ну или там уже почти бессмертный, который на этой планете от её самого зарождения, ещё когда только Солнце только-только сформировалось как звезда, и вот это газопылевое облако, 
			вот, после взрыва, Солнца, когда оно вспыхнуло, как звезда, начало формировать вот эти коацерваты, планеты, понимаешь, 
			я на этой Земле уже как будто почти пять миллиардов лет живу и знаю её вдоль и поперёк этот весь мир, а ты мне какие-то... мне не важно на твои тачки, на твои яхты, на твои квартиры, там, на твоё благо.
			Я был на этой планете бесконечным множеством, и круче Цезаря, и круче Гитлера, и круче всех великих, понимаешь, был, а где-то был конченым говном, ещё хуже, чем здесь. 
			''')
		sleep(1)
		await message.channel.send(''' Я множество этих состояний чувствую. Где-то я был больше подобен растению, где-то я больше был подобен птице, там, червю, где-то был просто сгусток камня, это всё есть душа, понимаешь? 
			Она имеет грани подобия совершенно многообразные, бесконечное множество. Но тебе этого не понять, поэтому ты езжай себе , мы в этом мире как бы живем разными ощущениями и разными стремлениями, соответственно, разное наше и место, разное и наше распределение. 
			Тебе я желаю все самые крутые тачки чтоб были у тебя, и все самые лучше самки, если мало идей, обращайся ко мне, я тебе на каждую твою идею предложу сотню триллионов, как всё делать.
			Ну а я всё, я иду как глубокий старец,узревший вечное, прикоснувшийся к Божественному, сам стал богоподобен и устремлен в это бесконечное, и который в умиротворении, покое, гармонии, благодати, в этом сокровенном блаженстве пребывает, 
			вовлеченный во всё и во вся, понимаешь, вот и всё, в этом наша разница. Так что я иду любоваться мирозданием, а ты идёшь преисполняться в ГРАНЯХ каких-то, вот и вся разница, понимаешь, ты не зришь это вечное бесконечное, оно тебе не нужно.
			Ну зато ты, так сказать, более активен, как вот этот дятел долбящий, или муравей, который очень активен в своей стезе, поэтому давай, наши пути здесь, конечно, имеют грани подобия, потому что всё едино, но я-то тебя прекрасно понимаю, 
			а вот ты меня - вряд ли, потому что я как бы тебя в себе содержу, всю твою природу, она составляет одну маленькую там песчиночку, от того что есть во мне, вот и всё, поэтому давай, ступай, езжай, а я пошел наслаждаться прекрасным осенним закатом на берегу теплой южной реки. 
			Всё, ступай, и я пойду. ''')




#Command help

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def help( ctx ):
	emb = discord.Embed( title = 'Commands for users', colour = discord.Color.red() )

	emb.add_field( name = '{}time'.format( '$' ), value = 'Данные о дате и времени' )
	emb.add_field( name = '{}join'.format( '$' ), value = 'Подключить бота к каналу' )
	emb.add_field( name = '{}leave'.format( '$' ), value = 'Отключить бота' )
	emb.add_field( name = '{}play'.format( '$' ), value = 'Включить музыку' )
	emb.add_field( name = '{}hello @user'.format( '$' ), value = 'Передать привет' )
	emb.add_field( name = '{}fuck @user'.format( '$' ), value = 'Послать' )
	emb.add_field( name = '{}anecdot @user'.format( '$' ), value = 'Попросить рассказать анекдот' )
	emb.add_field( name = '{}call @user'.format( '$' ), value = 'Позвать пользователя' )
	emb.add_field( name = '{}shit @user'.format( '$' ), value = 'Оскорбить пользователя' )
	emb.add_field( name = 'Созвать сервер'.format( '$' ), value = 'Созывает весь сервер' )
	emb.add_field( name = 'Преисполнение'.format( '$' ), value = 'Преисполниться в совём познании' )
	emb.add_field( name = 'анекдот'.format( '$' ), value = 'Бот расскажет анекдот' )
	



	await ctx.send( embed = emb )



@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def help_admin( ctx ):
	emb = discord.Embed( title = 'Commands for administrators', colour = discord.Color.red() )

	emb.add_field( name = '{}clear'.format( '$' ), value = 'Очистить чат' )
	emb.add_field( name = '{}kick'.format( '$' ), value = 'Кикнуть пользователя' )
	emb.add_field( name = '{}ban'.format( '$' ), value = 'Забанить пользователя' )
	emb.add_field( name = '{}unban'.format( '$' ), value = 'Разбанить пользователя' )
	emb.add_field( name = '{}time'.format( '$' ), value = 'Данные о дате и времени' )
	emb.add_field( name = '{}join'.format( '$' ), value = 'Подключить бота к каналу' )
	emb.add_field( name = '{}leave'.format( '$' ), value = 'Отключить бота' )
	emb.add_field( name = '{}play'.format( '$' ), value = 'Включить музыку' )
	emb.add_field( name = '{}hello @user'.format( '$' ), value = 'Передать привет' )
	emb.add_field( name = '{}fuck @user'.format( '$' ), value = 'Послать' )
	emb.add_field( name = '{}anecdot @user'.format( '$' ), value = 'Попросить рассказать анекдот' )
	emb.add_field( name = '{}call @user'.format( '$' ), value = 'Позвать пользователя' )
	emb.add_field( name = '{}shit @user'.format( '$' ), value = 'Оскорбить пользователя' )
	emb.add_field( name = 'Созвать сервер'.format( '$' ), value = 'Созывает весь сервер' )
	emb.add_field( name = 'анекдот'.format( '$' ), value = 'Бот расскажет анекдот' )
	emb.add_field( name = 'Преисполнение'.format( '$' ), value = 'Преисполниться в совём познании' )



	await ctx.send( embed = emb )


#Time
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def time( ctx, member = discord.Member ):
	emb = discord.Embed( title = 'Время и дата', description = 'Актуальные данные', colour = discord.Color.green(), url = 'https://www.timeserver.ru/cities/ru/khabarovsk' )

	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = '' )
	emb.set_image( url = 'https://media.tenor.com/images/91d0b45d95b27080c4d0d1175d586533/tenor.gif' )
	emb.set_thumbnail( url = 'https://cdn.discordapp.com/attachments/711533586695585874/769535941026381844/time.png' )

	now_date = datetime.datetime.now()


	emb.add_field( name = '   Дата:                    Время:', value = '{}'.format( now_date ) )

	await ctx.send( embed = emb )






#Interaction
@client.command( pass_context = True )
async def call( ctx, member: discord.Member):
	await member.send( f'{ member.mention }! Тебя вызывает - { ctx.author.mention } ' )

@client.command( pass_context = True )
async def fuck( ctx, member: discord.Member ):
	await member.send( f'{ member.mention }! Тебя послал нахуй - { ctx.author.mention }' )
	
@client.command( pass_context = True )
async def shit( ctx, member: discord.Member ):
	await member.send( f'{ member.mention }! Он - { ctx.author.mention }, говорит что ты ДИЗЕЛЬНЫЙ ЕБЛАН))' )
	
@client.command( pass_context = True )
async def anecdot( ctx, member: discord.Member ):
	await member.send( f'{ member.mention }! Тебя просят рассказать анекдот в чате канала!' )
	
@client.command( pass_context = True )
async def send_a( ctx ):
	await ctx.author.send( 'Привет, ты ДИЗЕЛЬНЫЙ ЕБЛАН!' )

@client.command( pass_context = True )
async def hello( ctx, member: discord.Member ):
	await member.send( f'{ member.mention }! Привет от - { ctx.author.mention }' )





#Role

@client.event
async def on_member_join( member ):
	channel = client.get_channel( 768917649144545340 )

	role = discord.utils.get( member.guild.roles, id = 768877598545281045 )

	await channel.send( embed = discord.Embed( description = f'Привет { member.mention }! Рады приветствовать тебя на нашем сервере!', colour = discord.Color.blue() ) )
	sleep(1)
	await channel.send( embed = discord.Embed( description =  f'Через 10 секунд тебе выдадут роль, благодаря которой, ты будешь иметь доступ к некоторым голосовым и текстовым каналам', colour = discord.Color.blue() ) )
	sleep(2)
	await channel.send( embed = discord.Embed( description = f'После чего, ты сможешь посетить канал - "roles", для получения общих и игровых ролей!', colour = discord.Color.blue() ) )
	sleep(10)
	
	await member.add_roles( role )
	



#Connecting voice chat
@client.command(pass_context = True)
async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		await ctx.send(f'Бот присоеденился к каналу: {channel}')


@client.command(pass_context = True)
async def leave(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()
		await ctx.send(f'Бот отключился от канала: {channel}')




#Play music
@client.command(pass_context = True)
async def play(ctx, url : str):
	song_there = os.path.isfile('song.mp3')

	try:
		if song_there:
			os.remove('song.mp3')
			print('[log] Старый файл удалён')
	except PermissionError:
		print('[log] Не удалось удалить файл')
	await ctx.send('Ожидайте')

	voice = get(client.voice_clients, guild = ctx.guild)

	ydl_opts = {
		'format' : 'bestaudio/best',
		'postprocessors' : [{
			'key' : 'FFmpegExtractAudio',
			'preferredcodec' : 'mp3',
			'preferredquality' : '192'
		}],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		print('[log] Загрузка...')
		ydl.download([url])

	for file in os.listdir('./'):
		if file.endswith('.mp3'):
			name = file
			print('[log] Переименновываю файл: {file}')
			os.rename(file, 'song.mp3')

	voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log] {name}, проигрывание завершено'))
	voice.source = discord.PCMVolumeTransformer(voice.source)
	voice.source.volume = 1

	song_name = name.rsplit('-', 2)
	await ctx.send(f'Сейчас играет: {song_name[0]}')





#Comand error
@clear.error
async def clear_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send( f'{ ctx.author.mention }, обязательно укажите аргумент!' )

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f'{ ctx.author.mention }, у вас недостаточно прав!' )


#Hello_World



#Connect

token = open( 'token.txt', 'r' ).readline()

client.run( token )



