import random
from wonderwords import RandomSentence


def get_sentence_to_type() -> tuple:
    # SENTENCES
    first = f"{s.sentence()[4:-1].capitalize()}, {s.bare_bone_sentence()[4:]}"
    second = random.choice(phrase_list)
    third = ", ".join(str(x) for x in adverbs_list_selected[:5])
    forth = f"{s.sentence()[4:-1].capitalize()}, {s.bare_bone_sentence()[4:]}"
    fifth = f"{s.sentence()[4:-1].capitalize()}, {s.bare_bone_sentence()[4:]}"
    sixth = random.choice(phrase_list)
    seventh = ", ".join(str(x) for x in adverbs_list_selected[5:])
    eight = f"{s.sentence()[4:-1].capitalize()}, {s.bare_bone_sentence()[4:]}"
    return first, second, third, forth, fifth, sixth, seventh, eight


adverbs = ['Now', 'Then', 'So', 'Very', 'Too', 'Never', 'Always', 'Ever', 'Seldom', 'Rarely', 'Gradually', 'Eventually',
           'Monthly', 'Weekly', 'Yearly', 'Annually', 'Quarterly', 'Much', 'Most', 'Quickly', 'Slowly', 'Incidentally',
           'Immediately', 'Simultaneously', 'Happily', 'Sadly', 'Frequently', 'Commonly', 'Sincerely', 'Faithfully',
           'Sweetly', 'Badly', 'Dearly', 'Patiently', 'Mostly', 'Silently', 'Willingly', 'Hardly', 'Often', 'Daily',
           'Occasionally', 'Regularly', 'Normally', 'Actually', 'Basically', 'Here', 'There', 'Yesterday', 'Today',
           'Tomorrow', 'Day after tomorrow', 'Day before yesterday', 'Tonight', 'Extremely', 'Exceedingly', 'Arguably',
           'Comparatively', 'Consecutively', 'Honestly', 'Truthfully', 'Lovingly', 'Perfectly', 'Highly', 'Likely',
           'Nearly', 'Barely', 'Far', 'Least', 'Deeply', 'Fully', 'Completely', 'Casually', 'Tastefully', 'Madly',
           'Purely', 'Privately', 'Publicly', 'Towards', 'Inside', 'Outside', 'Upstairs', 'Downstairs', 'Uphill',
           'Downhill', 'Everywhere', 'Somewhere', 'Nowhere', 'Anywhere', 'Eagerly', 'Beautifully', 'Proudly',
           'Elegantly', 'Confidently', 'Incessantly', 'Boldly', 'Carefully', 'Cautiously', 'Carelessly', 'Easily',
           'Awkwardly', 'Nearby', 'Cheerfully', 'Abruptly', 'Late', 'Everyday', 'Soon', 'Coldly', 'Angrily',
           'Curiously', 'Noisily', 'Loudly', 'Earnestly', 'Interestingly', 'Readily', 'Vaguely', 'Unwillingly',
           'Obediently', 'Rapidly', 'Continuously', 'Consciously', 'Instinctively', 'Boldly', 'Brightly', 'Cunningly',
           'Suitably', 'Appropriately', 'Currently', 'Doubtfully', 'Ambiguously', 'Momentarily', 'Early', 'Last week',
           'Last month', 'Last year', 'Later', 'Northwards', 'Southwards', 'Eastwards', 'Westwards', 'Forward',
           'Backwards', 'Away', 'In', 'Out', 'Under', 'Below', 'Above', 'Abroad', 'North', 'South', 'West', 'East',
           'Southeast', 'Southwest', 'Northeast', 'Northwest', 'Up', 'Down', 'Underneath', 'Gently', 'Superficially',
           'Supremely', 'Adequately', 'Comfortably', 'Conveniently', 'Generously', 'Briefly', 'Accidentally', 'Tightly',
           'Fearfully', 'Gracefully', 'Graciously', 'Busily', 'Randomly', 'Joyously', 'Mysteriously', 'Joyfully',
           'Poorly', 'Repeatedly', 'Seriously', 'Smoothly', 'Promptly', 'Roughly', 'Successfully', 'Sufficiently',
           'Skillfully', 'Sceptically', 'Differently', 'Physically', 'Psychologically', 'Logically', 'Analytically',
           'Graphically', 'Loosely', 'Fiercely', 'Unexpectedly', 'Tactfully', 'Lazily', 'Tremendously', 'Vicariously',
           'Vividly', 'Cleverly', 'Victoriously', 'Widely', 'Well', 'Purposefully', 'Wisely', 'Properly', 'Sickly',
           'Legally', 'Nicely', 'Legibly', 'Thoroughly', 'Shortly', 'Simply', 'Tidily', 'Necessarily', 'Tenaciously',
           'Strongly', 'Humbly', 'Consequently', 'Similarly', 'Unlikely', 'Possibly', 'Probably']

phrase = """Yeah, right. You're kidding. You're pulling my leg.
That's a bit of an exaggeration. He's stretching the truth.
He's not telling the whole truth. Being economical with the truth.
His story is fishy. That's an outright lie. That's a pack of lies.
They got off on the wrong foot. He got on the teacher's bad side.
She took offense at his comment. He has a chip on his shoulder.
He has a short fuse. he dissed my mother. Got his nose out of joint.
It's as light as a feather. As dry as a bone, as @strong as an ox.
It's as flat as a pancake. He's as mad as a hornet.
It's as old as the hills. It's as quick as lightning.
She's as sick as a dog. They're as different as night and day.
She's as stubborn as a mule. He's as proud as a peacock.
She's as white as a sheet. It's as solid as a rock.
It's as clear as mud, "I couldn't wait to get back home."
What's the matter?. What's wrong?. Are you all right?
You look a bit down. Is there anything I can do to help?
Cheer up! Chin up! It's not so bad. Everything will be OK.
Look on the bright side. It's not the end of the world.
It's fascinating. I couldn't tear myself away.
I couldn't put it down. I was so into it, I lost track of time.
It does nothing for me. I was bored to tears. It's intriguing.
I was bored to death. I was dying of boredom.
It's about as exciting as watching paint dry. I'm absolutely sure.
I'm positive that it will work. I'm a hundred percent certain.
Chances are that (this will probably happen).
I seriously doubt it. I don't think so. Probably not.
It's not very likely. There's not much chance of that.
I'd be very surprised if that happened. I wouldn't bet on it
You look nice / You look amazing! What a beautiful [@necklace]!
I like your [shirt/shoes/haircut/etc.]. The color is perfect!
You're a fantastic cook. My compliments to the chef!
3. What a nice apartment! 4. You have a beautiful home.
He's/She's so cute! Your kids are a lot of fun.
Lucky you! That was a stroke of luck "sudden event of good luck".
Some people have all the luck. As luck would have it (by chance)
He's down on his luck. "having a long period of difficulty"
I'm debating between [option A & B], I'm yet to make up my mind.
I'm on the fence, "I'm in the middle, I don't know what to decide)."
I'll take that into consideration. On the other hand…
I'm having second thoughts "I'm reconsidering my decision"
I changed my mind. He convinced/persuaded me to…
Looking back, I know it was the right decision. It's up to you
Could you give me a minute? (informal) Hang on a sec / Just a sec.
Hold on. Let me see/think. I'll be right with you. Bear with me.
That'll have to wait. Be patient. Not so fast! Hold your horses!
She was born to dance. He's a natural. He could do it in his sleep.
15. He knows it inside out. Call +1 903 395 3804
She knows [New York] like the back of her hand.
She's a walking encyclopedia of [philosophy]. In a class of his own.
He's the best in the business. She's very gifted.
He's a [chemistry] whiz. No comment. Check pink1398@gmail.com
I'm not at liberty to say to give out such information.
Wait and see, "You will discover the answer later"
Let me get back to you. (I will give you the answer later)
I'm sorry, that's confidential. I'm sorry, that's personal.
I'd rather not talk about it. It's none of your business.
1. Mind your own business. 2. Why do you want to know?
""".split("\n ")

s = RandomSentence()
adverbs_list_selected = [random.choice(adverbs) for x in range(10)]
phrase_list = phrase[0].split("\n")

tip_1 = "Use the correct starting position.\n\nWhen practicing your typing skills, " \
        "it's important to use proper hand placement. To start, keep your fingers " \
        "positioned over the home row keys (left hand over the A, S, D, and F keys, " \
        "and the right hand over the J, K, L, and ; keys).\n\nWith your thumbs hovering over the space bar. " \
        "From here, you can move your fingers slightly to reach neighboring keys."

tip_2 = "Don't look down your hands.\n\nInstead of looking down at your hands, focus on your screen. " \
        "This can be difficult at first, especially if you have not yet mastered the exact placement of the keys." \
        "\n\nHowever, looking at the screen will help improve your accuracy because you will be able to catch your " \
        "typos as they occur. You'll also begin to memorize the placement of the keys, so you'll be able to " \
        "type more quickly as you practice."
