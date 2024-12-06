from wordcloud import WordCloud
import nltk
from collections import Counter
from myfunctions import findtags
import matplotlib.pyplot as plt


# open으로 txt파일을 열고 read()를 이용하여 읽는다.
text = '''
So I have read an awful lot of negative comments about the new "Charlie and the Chocolate Factory". I myself have actually had the amazing chance to see a sneak preview of this movie in a contest and would like to put MY two cents worth in.
This is most definitely not a movie for young children with its hidden jokes and bizarre jumping about. A magical menagerie of color and wit with some very dark and eerie elements, this is a refreshing change from the very happy go lucky type movie that made up the original. While no one will ever be able to replace the truly amazing Gene Wilder as quirky chocolatier Willy Wonka, Johnny Depp adds new life and oddity to the character. The character of Charlie was wonderfully cast, using young Freddie Highmore to play him. The necessary chemistry required to make a movie actually work was extremely noticeable between Depp and Highmore because of their work together in the drama "Finding Neverland".
All in all I thought "Charlie and the Chocolate Factory" was a wonderful movie but definitely not for the children.
I was extremely pleased with the new Charlie and The Chocolate Factory movie, remake of the 70's Willy Wonka and the Chocolate Factory. Tim Burton did an excellent job recreating the original lines and incorporating his own interpretation, which made this 2005's version exciting, comedic and entertaining. I loved the mix of characters that starred - some rookies and some vets - their roles were played magnificently. I was also very pleased with Johnny Depp's performance in relation to the original Willy Wonka. I arrived thinking his role was going to be like most every other role he's played, with his own attitude. But, it was totally different from what everyone was used to, and it was hilarious. I loved the mix of sarcasm and comedy. The audience was full of a mix of different ages and everyone was laughing and really getting into it. The end was one of the best parts because everyone thought it was going to end negatively, but of course they made it even better than the original. Everyone was on their feet and clapping for a job well done. Tim Burton, Johnny Depp - Bravo!
Story- The screenplay is closer to Dahl's original book, but it does more - This new version of Charlie and the Chocolate factory plays on a deeper level, as we learn more about Willy Wonka. This movie fills in the gaps of the 70's version and makes many things clear from start to finish. From that, what we get is a deeper story, which is what we all want in a movie. That's what makes this so good. It doesn't end so abruptly like the first movie did. We all know that Charlie wins the chocolate factory but by the end of the movie, the real winner is Willy Wonka himself.
Acting- Perhaps its the charisma and great acting of Johnny Depp that makes it so incredible. He does a great job in every frame with his facial expressions. I also liked the new Charlie Bucket by Freddie Highmore; he brings a special innocence to the screen. Its nice to have Charlie's dad in the movie, as he was in the book. Grandpa Joe is very cheesy esp. when they find the golden ticket, but what do you expect? A lot of the characters are cheesy because we know the story, and know what's going to happen, so the writers and actors just have fun with that. The 4 other children are very similar to the old movie which works perfectly. And I laughed out loud every time the Oompa Loompas started to sing, cause we all know they are going to and the new songs are so cheesy.
Visuals- Charlie and the Chocolate Factory boasts visuals and special effects from scenes in the book that the original movie could not do. The nut room which was in the book, was in this movie. Fudge Mountain was shown, and much more CG images that Dahl envisioned. Even the opening credits are fun to watch. With more visuals, more can be shown and thus explained. Its visuals and story work hand in hand.
Overall - Go see this movie. If you appreciate a good movie that makes you think and somewhat cry, you will enjoy this. I generally dislike Tim Burton's work, but this is an exception I think anyone will like. I believe this movie was better than the first and am sure you will agree too.
If you have been a Burton and Depp fan since Edward Scissorhands, you will find their interpretation of Roald Dahl's Charlie and the Chocolate Factory to be a tasty treat. The sets, the costumes, Depp's performance as the phobic Wonka, go beyond eye candy. A real feast! And Elfman's soundtrack manages to extract some of the most embarrassing tunes from the 1960s (ones that we wished would have remained buried in the deepest recesses of our memories) to add an equally memorable and entertaining audio experience. Freddie Highmore once again delivers a performance that makes us wish he will never grow up, as all young actors do. So grab your Wonka bars and golden tickets and head out to the theater. This is one movie you really should see on the big screen.
'''
tokens = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(tokens)

jj_tags = findtags('JJ', pos_tags)
jjr_tags = findtags('JJR', pos_tags)
jjs_tags = findtags('JJS', pos_tags)

all_adjectives = []
for tag_dict in [jj_tags, jjr_tags, jjs_tags]:
    for word_list in tag_dict.values():
        all_adjectives.extend(word_list)

combined_adjectives = Counter(dict(all_adjectives))

most_common_adjectives = combined_adjectives.most_common(40)

print(most_common_adjectives)


# WordCloud를 생성한다.
# 한글을 분석하기위해 font를 한글로 지정해주어야 된다. macOS는 .otf , window는 .ttf 파일의 위치를
# 지정해준다. (ex. '/Font/GodoM.otf')
wc = WordCloud(background_color="white", max_font_size=60)
cloud = wc.generate_from_frequencies(dict(most_common_adjectives))

plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()

